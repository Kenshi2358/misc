"""
Takes in 2 csv files and loads them both into a dataframe.
Then compares them based on the address fields.
Returns only the non-matching records.
"""
# Standard library imports
import argparse
import inspect
import os
import sys

# 3rd party imports
import pandas as pd

# The 1st item in sys.path is this script's path.
# We're adding the parent directory as the 2nd item in sys.path.
# This is the only known way to add the settings.py file from the main directory.
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(1, parent_dir)

# Local application imports
from settings import logger

parser = argparse.ArgumentParser()

parser.add_argument("-f1", "--file1", type=str, required=True)
parser.add_argument("-f2", "--file2", type=str, required=True)

args = parser.parse_args()
file1 = args.file1
file2 = args.file2

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

fields_to_compare = ['address', 'city', 'state_code', 'postal_code']

# Merge the dataframes based on the fields_to_compare, using full outer join.
# An additional field gets created called '_merge'.
# This tells us if it exists in both dataframes, or only one of them.
# Adding indicator=True adds a column to the df output called "_merge".
merged_df = df1.merge(df2, on=fields_to_compare, how='outer', indicator=True)

non_matching_records = merged_df[merged_df['_merge'] != 'both']

# When you merge 2 dataframes, if columns have the same name in both dataframes,
# pandas appends suffixes to distinguish them. By default it uses _x and _y.
# _x is added to columns from the 1st df. _y is added to columns from the 2nd df.
output_str = f"""Non matching records:
{non_matching_records[['address_id_x', 'address_id_y', 'address', 'city', 'state_code', 'postal_code', '_merge']]}
"""

logger.info(output_str)

# Print off the counts of the merge field.
logger.info(merged_df['_merge'].value_counts())
