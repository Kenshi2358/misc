"""
This script takes in a table from a database/server and outputs:
An excel file containing counts of all non-null values.
Additionally, it contains distribution counts for each value in each column.
"""

# Standard library imports
import argparse
import sys
import os

# 3rd party imports
import pandas as pd
from openpyxl import load_workbook
import boto3
# import matplotlib.pyplot as plt

# Adding relative path.
sys.path.append("..")
from db_class import DB_Helper

# Custom imports
import settings
from settings import logger


def convert_tuples(column_tuples):
    """
    Converts a list of tuples back into a one dimensional list.
    """

    two_dimensional_column_list = list(map(list, column_tuples))

    fixed_list = []
    for each_row in two_dimensional_column_list:
        for each_item in each_row:
            fixed_list.append(each_item)

    return fixed_list


def determine_column_name(all_columns_dictionary: dict, name_list: list):
    """
    Determine the column name using the name_list and searching among all_columns_dictionary.
    """

    name_guess = ''

    # Check for the name using an exact match.
    end_loops = False
    for each_column in all_columns_dictionary:

        if end_loops == True:
            break

        for each_word in name_list:

            if each_column == each_word:
                name_guess = each_column
                end_loops = True
                break # Found an exact match. End both loops.

    # If still not found, check using a contains match.
    end_loops = False
    if name_guess == '':

        for each_column in all_columns_dictionary:

            if end_loops == True:
                break

            for each_word in name_list:

                if each_column.find(each_word) >= 0:
                    name_guess = each_column
                    end_loops = True
                    break # Found a contains match. End both loops.

    # If no name is found, return null string.
    if name_guess == '':
        name_guess = 'null'

    return name_guess


def create_address1_code(all_columns_dictionary):
    """
    Creates address1 sql code.
    """

    address1_list = ['address1', 'address_1', 'address']
    address1_g = determine_column_name(all_columns_dictionary, address1_list)

    address2_list = ['address2', 'address_2']
    address2_g = determine_column_name(all_columns_dictionary, address2_list)

    address3_list = ['address_suite', 'addresssuite']
    address3_g = determine_column_name(all_columns_dictionary, address3_list)

    two_address_boolean = False
    three_address_boolean = False
    if address1_g != address2_g:
        if (address1_g != 'null') and (address2_g != 'null'):
            two_address_boolean = True
            if address3_g not in (address1_g, address2_g):
                if address3_g != 'null':
                    three_address_boolean = True

    city_list = ['city']
    city_g = determine_column_name(all_columns_dictionary, city_list)

    state_list = ['state']
    state_g = determine_column_name(all_columns_dictionary, state_list)

    zip_list = ['zipcode', 'zip_code', 'zip']
    zip_g = determine_column_name(all_columns_dictionary, zip_list)

    phone_list = ['phonenumber', 'phone_num', 'phone']
    phone_g = determine_column_name(all_columns_dictionary, phone_list)

    fax_list = ['faxnumber', 'fax_num', 'fax']
    fax_g = determine_column_name(all_columns_dictionary, fax_list)

    # Create a long string to output.
    long_str = """
    select1="
    select t.*
    into schema2.table2
    from (
        select distinct
            blah1,
            blah2,
            blah3,
            """

    if three_address_boolean == True:
        long_str += f"""
            replace(replace(replace(concat({address1_g}, ' ', {address2_g}, ' ', {address3_g}), ' ', '<>'), '><', ''), '<>', ' ') as addr_line1,
            """
    elif two_address_boolean == True:
        long_str += f"""
            concat({address1_g}, ' ', {address2_g}) as addr_line1,
            """
    else:
        long_str += f"""
            {address1_g} as addr_line1,
            """

    long_str += f"""
            {city_g} as city,
            {state_g} as state,
            substring({zip_g}, 1, 5) as zip,
            """

    if len(phone_g) > 0:
        long_str += f"""
            case when {phone_g} is not null then {phone_g}
            end as addr_phone1_number,
            """

    if len(fax_g) > 0:
        long_str += f"""
            case when {fax_g} is not null then {fax_g}
            end as addr_phone2_number,
            """

    # If last character is a comma, remove it.
    if long_str[-1] == ',':
        long_str = long_str[:-1]

    long_str += """
        from schema1.table1
        where some_clause
    ) as t;"
    """

    return long_str


def create_address2_code(all_columns_dictionary):
    """
    Creates address2 sql code.
    """

    gender_list = ['gender']
    gender_g = determine_column_name(all_columns_dictionary, gender_list)

    address1_list = ['address']
    address1_g = determine_column_name(all_columns_dictionary, address1_list)

    address2_list = ['address2', 'address_2']
    address2_g = determine_column_name(all_columns_dictionary, address2_list)

    address3_list = ['address_suite', 'addresssuite']
    address3_g = determine_column_name(all_columns_dictionary, address3_list)

    two_address_boolean = False
    three_address_boolean = False
    if address1_g != address2_g:
        if (address1_g != 'null') and (address2_g != 'null'):
            two_address_boolean = True
            if address3_g not in (address1_g, address2_g):
                if address3_g != 'null':
                    three_address_boolean = True

    city_list = ['city']
    city_g = determine_column_name(all_columns_dictionary, city_list)

    state_list = ['state']
    state_g = determine_column_name(all_columns_dictionary, state_list)

    zip_list = ['zipcode', 'zip_code', 'zip']
    zip_g = determine_column_name(all_columns_dictionary, zip_list)

    # Create a long string to output.
    pro_str = f"""
    select2="
    select t.*
    into schema4.table4
    from (
        select distinct
            blah1,
            blah2,
            blah3,
            {gender_g} as gender,
            """

    if three_address_boolean == True:
        pro_str += f"""
            replace(replace(replace(concat({address1_g}, ' ', {address2_g}, ' ', {address3_g}), ' ', '<>'), '><', ''), '<>', ' ') as addr_line1,
            """
    elif two_address_boolean == True:
        pro_str += f"""
            concat({address1_g}, ' ', {address2_g}) as addr_line1,
            """
    else:
        pro_str += f"""
            {address1_g} as addr_line1,
            """

    pro_str += f"""
            {city_g} as city,
            {state_g} as state,
            substring({zip_g}, 1, 5) as zip,
            """

    # If last character is a comma, remove it.
    if pro_str[-1] == ',':
        pro_str = pro_str[:-1]

    pro_str += """
        from schema3.table3
        where some_clause
    ) as t;"
    """

    return pro_str


def create_correlation_tab(writer: pd.ExcelWriter, df: pd.DataFrame, filtered_non_null_dictionary: dict) -> None:
    """
    Runs category correlation stats between columns.
    The Pearson correlation measures the strength of the linear relationship between two variables.
    It has a value between -1 to 1, with a value of -1 meaning a total negative linear correlation,
    0 meaning no correlation, and + 1 meaning a total positive correlation.
    0.7 or higher is considered a strong correlation.

    Look for an address column.
    If found, look for an extid column.
    If found, convert data type to category and run correlation between the columns.
    """

    address_keywords_list = ['address']
    extid_keywords_list = ['url', 'phone']

    address_columns = []
    extid_columns = []

    # Get the list of columns. The find method is case sensitive.
    for each_key in filtered_non_null_dictionary:

        for each_address in address_keywords_list:
            if each_key.find(each_address) >= 0:
                if each_key not in address_columns:
                    address_columns.append(each_key)

        for each_extid in extid_keywords_list:
            if each_key.find(each_extid) >= 0:
                if each_key not in extid_columns:
                    if each_key not in address_columns:
                        extid_columns.append(each_key)

    if len(address_columns) > 0 and len(extid_columns) > 0:

        # Create new dataframe from existing dataframe.
        new_list = []
        for x in address_columns:
            new_list.append(x)
        for y in extid_columns:
            new_list.append(y)

        df2 = df[new_list].copy()

        # View new dataframe.
        logger.debug(df2)

        # Convert all datatypes to category types.
        # .cat.codes converts your category from a string representation to an integer representation.
        # Example: 0's and 1's.
        for each_column in df2:
            logger.debug(f'Converting {each_column} to category type.')
            df2[each_column] = df2[each_column].astype('category').cat.codes

        # Run correlation on these columns and save to an excel tab.
        logger.debug(df2.corr())
        logger.info('Saving Correlation tab.')
        df2.corr().to_excel(writer, sheet_name='Correlation', freeze_panes=(1, 1))


def create_one_column_tabs(writer: pd.ExcelWriter, df: pd.DataFrame, filtered_non_null_dictionary: dict) -> int:
    """
    Create 1 column distinct counts for each column.
    Only view columns if the unique record set is under 10k records.
    """

    column_count = 0
    for each_key in filtered_non_null_dictionary:

        current_class = df[each_key].value_counts()
        if current_class.size < 10000:

            sheet_name1 = each_key
            if len(sheet_name1) > 31:
                sheet_name1 = sheet_name1[0:31]

            df[each_key].value_counts().to_excel(writer, sheet_name=sheet_name1, freeze_panes=(1, 1))
            column_count += 1
            # plt.plot(df[each_key].value_counts())
            # pass

    return column_count


def create_two_column_tabs(writer: pd.ExcelWriter, df: pd.DataFrame, sorted_dictionary: dict) -> int:
    """
    Create 2 column pivot tables using sorted_dictionary.
    Create up to 40 of these tables/tabs.

    The columns are chosen based on:
    a) the # of uniques.
    b) Using that column a max of 5 times.
    c) Not containing forward slashes or colons.
    """

    used_count_dict = {}
    max_two_column_tables = 40
    num_repeat_columns = 5

    column_count = 0

    for each_key1 in sorted_dictionary:
        for each_key2 in sorted_dictionary:
            if each_key1 != each_key2:

                # Initial values.
                key1_exists = False
                key2_exists = False

                if each_key1 in used_count_dict:
                    key1_exists = True
                if each_key2 in used_count_dict:
                    key2_exists = True

                if (key1_exists and used_count_dict[each_key1] < num_repeat_columns) or (key1_exists is False):
                    if (key2_exists and used_count_dict[each_key2] < num_repeat_columns) or (key2_exists is False):
                        if column_count < max_two_column_tables:

                            sheet_name1 = f'{each_key1}-{each_key2}'

                            # Truncate sheet name down to 31 characters if needed.
                            if len(sheet_name1) > 31:
                                sheet_name1 = sheet_name1[0:31]

                            pd.crosstab(df[each_key1], df[each_key2]).to_excel(writer, sheet_name=sheet_name1, freeze_panes=(1, 1))
                            column_count += 1

                            if key1_exists:
                                used_count_dict[each_key1] += 1
                            else:
                                used_count_dict[each_key1] = 1

                            if key2_exists:
                                used_count_dict[each_key2] += 1
                            else:
                                used_count_dict[each_key2] = 1

        return column_count


def prettify_workbook(full_path: str) -> None:
    """
    Cleans up the workbook to make it more read-able to the end user.
    """

    # Re-open and set the zoom level.
    wb = load_workbook(filename=full_path)

    for each_sheet in wb.worksheets:
        each_sheet.sheet_view.zoomScale = 150

        # Define column widths to make file pretty.
        dims = {}
        for row in each_sheet.rows:
            for cell in row:
                if cell.value:
                    dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))
        for col, value in dims.items():
            if value < 8:
                each_sheet.column_dimensions[col].width = 8
            elif value > 36:
                each_sheet.column_dimensions[col].width = 36
            else:
                each_sheet.column_dimensions[col].width = value

    wb.save(full_path)
    logger.info(f'Saving workbook to {full_path}')


def main(args):
    """
    Main function to retrieve records, store them into a dataframe, and output stats.
    """

    # Required
    db_host = args.db_host
    db_name = args.db_name
    schema_table_name = args.table_name
    username = args.username

    # Optional
    temp_path = args.path
    bucket = args.bucket
    sql_only = args.sql_only

    # Connect to the correct database.
    wh_connection = DB_Helper(host=db_host, database=db_name, user=username)
    logger.main(f"Connected to database: {db_name}")

    new_table_list = schema_table_name.split('.')
    if len(new_table_list) != 2:
        logger.critical("Need schema and table in the table parameter, separated by a period.")
        exit(1)

    my_schema = new_table_list[0]
    my_table = new_table_list[1]

    # --------------------------------

    # Get a list of all columns.
    my_string1 = f"""
    select column_name
    from information_schema.columns
    where table_name = '{my_table}'
    order by ordinal_position
    """

    # Get the record count.
    my_string2 = f"""
    select count(*)
    from {my_schema}.{my_table}
    """

    value_tuples = wh_connection.query(my_string1, return_data=True)
    column_name_list = convert_tuples(value_tuples)

    record_count = convert_tuples(wh_connection.query(my_string2, return_data=True))

    logger.info(f'{len(column_name_list)} total columns, with {record_count[0]:,} records.')

    # Create a dictionary of key-value pairs, where
    # key is the column name and value is the count.
    column_counts_dictionary = {}

    # Loop through each column name and add the count to the dictionary.
    for each_column_name in column_name_list:

        my_string3 = f"""
        select count(*) from {my_schema}.{my_table}
        where {each_column_name} is not null
        """

        value_tuples = wh_connection.query(my_string3, return_data=True)
        current_column_count = convert_tuples(value_tuples)

        column_counts_dictionary[f'{each_column_name}'] = current_column_count[0]

    # Filter to find only columns that have at least one non-null value.
    filtered_non_null_dictionary = {a: b for a, b in column_counts_dictionary.items() if b > 0}

    # ===================================================

    # Create sql code for however many sections are needed.
    address1_str = create_address1_code(filtered_non_null_dictionary)
    address2_str = create_address2_code(filtered_non_null_dictionary)

    logger.info('Creating sql_generation.sh file.')
    all_lines_list = [address1_str, address2_str]

    # -----------------------------------
    # Decide where to save the shell file and what to name it.
    if temp_path is None:
        temp_path = ''

    shell_name = 'table_results_sql_generation.sh'
    full_path = f'{temp_path}{shell_name}'

    with open(full_path, 'w', encoding="utf-8") as f:
        for each_line in all_lines_list:
            f.write(each_line)
            f.write('\n')
    # -----------------------------------

    # If bucket parameter exists, move file from temporary path to s3.
    if (bucket is not None) and (len(bucket) > 0):
        logger.main(f'Uploading file: {shell_name} to s3')

        first_forward_slash = bucket.find('/')
        if first_forward_slash == -1:
            logger.info("Could not find the forward slash in the output s3 string provided. Ending program early.")
            exit(1)

        s3_bucket = bucket[0:first_forward_slash]
        s3_key = bucket[(first_forward_slash + 1):]

        s3_name = s3_key + shell_name
        s3_client = boto3.client('s3')

        logger.info(f'full_path: {full_path} s3_bucket: {s3_bucket} s3_name: {s3_name}')

        s3_client.upload_file(full_path, s3_bucket, s3_name)

        if os.path.isfile(full_path) or os.path.islink(full_path):

            logger.info(f'Removing temporary file {shell_name} from server')
            os.unlink(full_path)

    if (sql_only is not None) and (len(sql_only) > 0):
        logger.info('sql_only parameter used. Only outputting sql_generation.sh file.')
        exit(1)

    # ===================================================
    # Load table into a pandas dataframe.
    logger.info('Started loading table into dataframe.')
    my_string4 = f"""
    select * from {my_schema}.{my_table}
    """

    all_data_tuples = wh_connection.query(my_string4, return_data=True)

    df = pd.DataFrame(data=all_data_tuples, columns=column_name_list)

    logger.info('Finished loading table into dataframe.')
    # To check the data types, type:
    # df.dtypes
    # ===================================================

    # ********************************************
    # Create a combined address column as new dataframe.
    combined_address_keywords = ['address', 'city', 'state', 'zip']
    combined_address_columns = []

    # Check if the address field is after the city field.
    # And line1 field is before the city field.
    # If so, replace address with line1 in the list.

    # Do this by creating a dictionary of variables containing the column position.
    # apd = address position dictionary.
    apd = {
        'address': 0,
        'city': 0,
        'line1': 0
    }

    for each_keyword in apd:
        i = 0
        for each_key in filtered_non_null_dictionary:
            i += 1
            if each_key.find(each_keyword) >= 0:
                apd[each_keyword] = i
                break

    if (apd['address'] > apd['city']) and (apd['city'] > 0):
        if (apd['line1'] < apd['city']) and (apd['line1'] > 0):
            combined_address_keywords[0] = 'line1'

    for addr_type in combined_address_keywords:
        for each_key in filtered_non_null_dictionary:
            if each_key.find(addr_type) >= 0:
                if each_key not in combined_address_columns:
                    combined_address_columns.append(each_key)
                    # exit loop early since we found the unique column for this keyword.
                    # Moves onto the next addr_type.
                    break

    if 'combined_address' not in filtered_non_null_dictionary:
        if len(combined_address_columns) == 4:

            logger.info(f'Started -- create combined_address column from: {combined_address_columns}')
            df['combined_address'] = df[combined_address_columns].astype(str).sum(axis=1)

            logger.info('Finished -- create combined address column.')

            # Add one more key to the filtered_non_null_dictionary:
            filtered_non_null_dictionary['combined_address'] = 1

    # ********************************************

    # ---------------------------------------------------
    # Get a dictionary of the # of unique values for each column.
    num_unique_series = df.nunique()
    num_unique_dict = num_unique_series.to_dict()

    max_num_uniques = 51

    # Remove columns that contain a date in it's first unique value.
    for each_key, each_value in list(num_unique_dict.items()):
        # sample the first non-null in each column and save it as a string.
        # Only check value counts greater than 1.

        if len(df[each_key].value_counts()) > 1:

            sample_string = next(iter(dict(df[each_key].value_counts())))
            sample_string = str(sample_string)

            # If it contains a date or time format, remove that column.
            # Defining formats as having: forward slashes or colons.
            forward_slash_count = sample_string.count('/')
            colon_count = sample_string.count(':')
            if forward_slash_count == 2:
                num_unique_dict.pop(each_key)
            elif colon_count >= 1:
                num_unique_dict.pop(each_key)

    # Remove columns that have unique counts of: 0, 1.
    # Remove columns until we have the 12 smallest columns left.
    while len(num_unique_dict) > 12:

        if max_num_uniques <= 4:
            break
        max_num_uniques -= 1

        for each_key, each_value in list(num_unique_dict.items()):
            if (each_value in (0, 1)) or (each_value >= max_num_uniques):
                num_unique_dict.pop(each_key)

    # ---------------------------------------------------

    sorted_dictionary = dict(sorted(num_unique_dict.items(), key=lambda item: item[1]))

    num_one_column_tables = 0
    num_two_column_tables = 0

    if temp_path is None:
        temp_path = ''

    filename1 = f'table_results_{my_table}.xlsx'
    full_path = f'{temp_path}{filename1}'

    # Output stats to an excel file.
    with pd.ExcelWriter(full_path) as writer:

        # Create Main tab.
        df.describe().transpose().to_excel(writer, sheet_name='Main', freeze_panes=(1, 1))

        create_correlation_tab(writer, df, filtered_non_null_dictionary)

        num_one_column_tables = create_one_column_tabs(writer, df, filtered_non_null_dictionary)
        num_two_column_tables = create_two_column_tabs(writer, df, sorted_dictionary)

        # Examples:
        # df.describe().transpose()
        # df['provider_degree'].value_counts()

    logger.info(f'Created {num_one_column_tables} tabs for 1 set columns.')
    logger.info(f'Created {num_two_column_tables} tabs for 2 set columns.')

    prettify_workbook(full_path)

    # If bucket parameter exists, move file from temporary path to s3.
    if (bucket is not None) and (len(bucket) > 0):
        logger.main(f'Uploading file: {filename1} to s3')

        first_forward_slash = bucket.find('/')
        if first_forward_slash == -1:
            logger.info("Could not find the forward slash in the output s3 string provided. Ending program early.")
            exit(1)

        s3_bucket = bucket[0:first_forward_slash]
        s3_key = bucket[(first_forward_slash + 1):]

        s3_name = s3_key + filename1
        s3_client = boto3.client('s3')

        logger.info(f'full_path: {full_path} s3_bucket: {s3_bucket} s3_name: {s3_name}')

        s3_client.upload_file(full_path, s3_bucket, s3_name)

        if os.path.isfile(full_path) or os.path.islink(full_path):

            logger.info(f'Removing temporary file {full_path} from server')
            os.unlink(full_path)


# Start Process.
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-db_host", "--db_host", type=str, help="db_host.", required=True)
    parser.add_argument("-db_name", "--db_name", type=str, help="db_name.", required=True)
    parser.add_argument("-table_name", "--table_name", type=str, help="table name including the schema", required=True)
    parser.add_argument("-username", "--username", type=str, help="username", required=True)

    parser.add_argument("-path", "--path", type=str, help="The local file path to save files.", required=False)
    parser.add_argument("-bucket", "--bucket", type=str, help="Where output file will be saved on s3.", required=False)
    parser.add_argument("-sql_only", "--sql_only", type=str, required=False)

    args = parser.parse_args()

    main(args)
