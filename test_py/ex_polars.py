# Standard Library imports
import argparse
import inspect
import math
import os
import sys

from datetime import datetime

# 3rd party imports
import polars as pl

# Add main directory to os.
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(1, parent_dir)

# Custom imports
import settings
from settings import logger


def get_total_num_batches(args) -> None:
    """
    Gets the total # of batches found in the file and prints it out
    """
    full_file_name = f"{args.local_path}{args.filename}"

    reader = pl.read_csv_batched(source=full_file_name, separator="|", infer_schema_length=0, low_memory=True)
    item_count = 0
    while True:
        batches = reader.next_batches(1)
        if not batches:
            break
        item_count += 1
    logger.info(f"Total # of batches in this file: {item_count}")


def write_to_database2(df: pl.DataFrame, table_name: str, connection_uri: str) -> None:
    logger.info("Starting table write")

    try:
        # Load 50,000 records as a time.
        chunk_size = 50_000

        num_chunks = math.ceil(len(df) / chunk_size)
        logger.info(f"{num_chunks} chunks to load this batch.")

        chunk_count = 1
        for i in range(0, len(df), chunk_size):
            chunk = df[i:i+chunk_size]

            chunk.write_database(
                table_name=table_name,
                connection=connection_uri,
                if_table_exists='append',  # 'replace' to truncate and reload, 'fail' to fail if exists, 'append' to append
                engine='sqlalchemy'
            )
            logger.info(f"chunk # {chunk_count} written to database")
            chunk_count += 1

        logger.info("All data written for this batch")

    except Exception as e:
        logger.error(f"Error writing to database: {e}")
        sys.exit(1)


def write_to_database(df: pl.DataFrame, table_name: str, connection_uri: str) -> None:
    """Writes df to database"""

    logger.info(f"Writing df to table_name: {table_name}")

    try:
        df.write_database(
            table_name=table_name,
            connection=connection_uri,
            if_table_exists='replace',  # 'replace' to truncate and reload
            engine='sqlalchemy'
        )
        logger.info("Data written to database")
    except Exception as e:
        logger.error(f"Error writing to database: {e}")
        sys.exit(1)


def main(args):
    """
    Main procedure for run.
    """

    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create an empty dataframe with 1 column defined.
    df1 = pl.DataFrame(schema={"column_id": pl.Int64})

    temp_table_name = ""
    connection_uri = f"postgresql://mdx@{args.server}:5432/{args.database}"
    type_code = ""
    file_list = []
    small_csv = True

    for each_file in file_list:

        if small_csv:
            # =======================
            # Small CSV file to load:
            # Read a csv into a polars dataframe.
            temp_file_path = ""
            temp_df = pl.read_csv(temp_file_path, encoding='windows-1252', infer_schema_length=None, separator=',', quote_char='"')

            # Update column names to lowercase. Update spaces to underscore.
            temp_df = temp_df.rename({col: col.lower().replace(" ", "_") for col in temp_df.columns})

            # Write each dataframe to it's own table.
            write_to_database(temp_df, temp_table_name, connection_uri)

        else:
            # =======================
            # Large CSV file to load:

            # Keeping in case we need to do data manipulation before loading.
            # Can run sql queries after loading.

            # # Dry run the reader to get the total # of batches.
            get_total_num_batches(args)

            reader = pl.read_csv_batched(source=each_file, separator="|", infer_schema_length=0, low_memory=True)
            batches = reader.next_batches(5)
            batch_count = 5
            print_first_header = True

            while batches:
                logger.info(f"Batch #'s {batch_count - 4} to {batch_count}")
                df_current_batches = pl.concat(batches)
                if print_first_header:
                    logger.info(df_current_batches.head(3))
                print_first_header = False

                write_to_database(df_current_batches, args.table_name, connection_uri)
                batches = reader.next_batches(5)
                batch_count += 5
            # =======================

        # Update temp_df with 2 new columns.
        temp_df = temp_df.with_columns([
            pl.lit(type_code).alias("type_code1"),
            pl.lit(current_timestamp).alias("file_download")
        ])

        # Read each file into the same dataframe.
        df1 = pl.concat([df1, temp_df], how='align')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("-s", "--server", type=str, help="the server in which the database exists", required=True)
    parser.add_argument("-d", "--database", type=str, help="the database in which the table will be created", required=True)
    parser.add_argument("-f", "--filename", type=str, help="the file to be parsed and inserted into a table", required=True)
    parser.add_argument("-t", "--table_name", type=str, help="name of table to be created", required=True)
    parser.add_argument("-sc", "--schema", type=str, help="schema where you want to table to be created", required=True)

    # Optional parameters
    parser.add_argument("-e", "--encoding", type=str, help="client's file", default="utf-8")
    parser.add_argument("-z", "--target_size_mb", type=int, help="Target file size of each split file in megabytes", default=2000)

    global_args = parser.parse_args()

    main(global_args)
