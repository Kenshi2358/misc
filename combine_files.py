"""
Takes in a list of files to combine, along with their s3 path.
Then moves the files to the server, combines them, and moves them back to s3.
"""
# Standard library imports
import argparse

# 3rd party imports
import pandas as pd

# Local application imports
from settings import logger

def main(args):

    logger.main("Starting file combine")

    file_list = args.file_list
    local_path = args.local_path
    delimiter1 = args.delimiter
    s3_inbound = args.s3_inbound

    logger.info(f"file_list: {file_list}  type: {type(file_list)}")

    dataframe_list = []
    for each_file in file_list:

        full_path = f"{local_path}{each_file}"
        df = pd.read_csv(full_path, delimiter=delimiter1)
        dataframe_list.append(df)

    logger.info("Combining all dataframes into one file")
    combined_df = pd.concat(dataframe_list, axis=1, ignore_index=True)

    logger.info("Writing combined_df to a combined file")
    sliced_filename = file_list[0][6:]
    new_filename = f"combined{sliced_filename}"
    full_path = f"{local_path}{new_filename}"
    combined_df.to_csv(full_path, sep=f'{delimiter1}', index=False)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_list", required=True, type=str)
    parser.add_argument("-i", "--s3_inbound", required=True)
    parser.add_argument("-l", "--local_path", required=True)
    parser.add_argument("-d", "--delimiter", required=True)

    args = parser.parse_args()

    main(args)
