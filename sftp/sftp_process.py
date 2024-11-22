"""
This script checks for files on an SFTP and s3.
If found, loads them onto the server.
"""

# Standard library imports
import argparse
import fnmatch
import inspect
import os
import subprocess
import sys

# 3rd party imports
import psycopg

# Add main directory to sys.
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(1, parent_dir)

# Local imports
from settings import logger

# custom class object for interacting with s3 objects.
from helpers.aws import S3


def s3_file_check(args) -> list:
    """
    View the contents of s3.
    """
    logger.main("Running s3_file_check")

    # initialize s3
    s3 = S3(args.s3_uri)
    s3_objects = s3.ls()

    matched_list = []

    if len(s3_objects) == 0:
        logger.warning(f"No files found in {args.s3_uri}.")

    for each_object in s3_objects:
        if fnmatch.fnmatch(each_object, f'*{args.file_pattern}*'):
            matched_list.append(each_object)

    logger.info(f"matched_files: {matched_list}")

    # Check that each_file has no spaces.
    for each_file in matched_list:
        if each_file.find(' ') >= 0:
            message1 = f"""
            file: {each_file} has a space in the filename.
            This will crash the loader.
            Please rename file and rerun.
            """
            logger.error(message1)
            exit(1)

    return matched_list


def raw_data_pull(args, file_list) -> None:
    """
    Pulls raw file from s3 to local server.
    """
    logger.main("Running raw_data_pull")

    s3 = S3(args.s3_uri)

    for each_file in file_list:
        logger.info(f"Pulling file: {each_file}")
        s3.download(each_file, f'{args.sftp_local_path}/')


def raw_to_db(args, file_list) -> None:
    """
    Loads the given file onto the database.
    """
    logger.main("Running raw_to_db")

    schema = args.input_schema_name
    table_name = args.input_table_name

    # Establish connection.
    conn = psycopg.connect(host=args.host, dbname=args.db, user=args.user)
    cursor = conn.cursor()
    logger.info(f"Connection established to {args.db} on {args.host}")

    # Truncate table if table exists.
    cursor.execute(f"truncate {schema}.{table_name};")
    conn.commit()
    logger.info(f"Truncating table: {schema}.{table_name}")

    # Load file to database.
    for each_file in file_list:
        logger.info(f"Using file: {each_file}")

        cursor.copy_expert(
            file=open(f"{each_file}"),
            sql=f"""
            COPY {schema}.{table_name}
            FROM stdin
            WITH CSV
            DELIMITER as '{args.delimiter}'
            QUOTE E'\b'
            NULL as ''
            """
        )
        conn.commit()
        logger.info(f"Loaded {args.each_file} into {schema}.{table_name}")


def main(args):
    """
    Main procedure for scheduled run.
    """
    logger.main("Starting main procedure")

    # s3 file check. If exists, skip SFTP step.
    matched_list = s3_file_check(args)
    if len(matched_list) == 0:
        # run SFTP step.
        sub_args = [
            "python", "sftp_process.py",
            "--actions", "d,p3",
            "--host", f"{args.sftp_host}",
            "--user", f"{args.sftp_user}",
            "--password", f"{args.sftp_password}",

            "--port", f"{args.sftp_port}",
            "--remote_path", f"{args.sftp_remote_path}",
            "--local_path", f"{args.sftp_local_path}",
            "--file_pattern", f"*{args.file_pattern}*",

            "--s3_uri", f"{args.s3_uri}",
            "--checksum", f"{args.sftp_checksum}",
            "--cleanup_process", f"{args.local_cleanup}"
        ]
        result = subprocess.run(sub_args, capture_output=True, text=True)

        # Check if SFTP step was successful.
        if result.returncode != 0:
            logger.info(f"Error during sftp_process.py: {result.stderr}")
            exit(1)
        else:
            logger.info("SFTP step successful")

        # Check s3 again.
        matched_list = s3_file_check(args)
        if len(matched_list) == 0:
            logger.critical("No files found to load. Ending script.")
            exit(1)

    # Pull file from s3 to local server.
    raw_data_pull(args, matched_list)

    # Load file to input table.
    raw_to_db(args, matched_list)

    # Perform any data transformations or checks.

    # Move file to s3 archives.


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # SFTP credentials.
    parser.add_argument("--sftp_host", required=True)
    parser.add_argument("--sftp_user", required=True)
    parser.add_argument("--sftp_password", required=True)

    parser.add_argument("--sftp_port", required=False, type=int, default=22)
    parser.add_argument("--sftp_remote_path", required=True)
    parser.add_argument("--sftp_local_path", required=True)
    parser.add_argument("--sftp_checksum", required=False, default="false")

    # Change local_cleanup default to 1 when done testing.
    parser.add_argument("--local_cleanup", required=False, default=0)
    parser.add_argument("--file_pattern", required=True)
    parser.add_argument("--s3_uri", required=True)

    # Database credentials.
    parser.add_argument("--host", required=True)
    parser.add_argument("--db", required=True)
    parser.add_argument("--user", required=False, default="des")

    parser.add_argument("--input_table_name", required=True)
    parser.add_argument("--input_schema_name", required=True)
    parser.add_argument("--delimiter", required=True)

    args = parser.parse_args()

    main(args)
