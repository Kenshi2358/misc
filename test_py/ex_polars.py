# Standard Library imports
import inspect
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

current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Create an empty dataframe with 1 column defined.
df1 = pl.DataFrame(schema={"column_id": pl.Int64})

temp_table_name = ""
connection_uri = ""
type_code = ""
file_list = []

for each_file in file_list:

    # Read a csv into a polars dataframe.
    temp_file_path = ""
    temp_df = pl.read_csv(temp_file_path, encoding='windows-1252', infer_schema_length=None, separator=',', quote_char='"')

    # Update column names to lowercase. Update spaces to underscore.
    temp_df = temp_df.rename({col: col.lower().replace(" ", "_") for col in temp_df.columns})

    # Write each dataframe to it's own table.
    write_to_database(temp_df, temp_table_name, connection_uri)

    # Update temp_df with 2 new columns.
    temp_df = temp_df.with_columns([
        pl.lit(type_code).alias("type_code1"),
        pl.lit(current_timestamp).alias("file_download")
    ])

    # Read each file into the same dataframe.
    df1 = pl.concat([df1, temp_df], how='align')

