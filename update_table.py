"""
This script updates a given table across one or more warehouses and servers.
It takes in a csv file containing all fields and value that need updating.

Then it loops through the specified warehouses and servers to find the matching table and columns.
If the schema, table, or column names do not exist: it skips this item and moves on.
If the schema, table, and colummn names all match: it makes an update.

The csv must contain a header row in the first row.
The csv must have a column that is the unique identifier for each record.
If it's not specified in the parameters, then the script defaults to using the first header column in the file.

When the insert option is chosen:
If entered value is not found, it will update the table with the new value.
If it already exists, it will continue to next item.

If the client name is not chosen:
It will check all active, provider warehouses, excluding datamarts and the deadpool server.

If you want to update a custom set of warehouses:
you need to create a custom sql query below and give it a client name.

Usage:
python3 update_table.py -a "rollback" -y "upsert" -t "schema_name.table_name" -csv "filename1.csv" -c "client1"
python3 update_table.py -a "rollback" -y "insert" -t "schema_name.table_name" -f "column1" -v "orange"

Parameters:
    Required:
    -a ["rollback", "update"]
        rollback - updates the given field for each table, then rolls back. Used for testing.
        update - updates the given field for each table.

    -y - insert type. Options ["insert", "upsert"].
    -t - enter table name including the schema. Example: schema_name.table_name

    Optional:
    -csv - csv_filename. Method to update many records and many fields into the same table.
    If a csv file is given, that is the source of field names and values to update.
    If a csv file is not given, t uses the f and v arguments given.

    -f - field 1 name. This is the primary field/column name. Can pipe delimit here for additional fields.
    -v - field 1 value. This is the primary field/column value. Can pipe delimit here for additional values.
    This is the old method. Limited to updating 1 record at a time.

    -c - client name. If user enters a value here, script will choose sql queries for that client name.
        This will give us the relevant servers and warehouses to check.

    -e - encoding type of the csv file. Default encoding: utf-8
    Loading a csv file without an encoding type can put a unicode character at the start of the file.
    This will error out the file load. To ensure this is covered, you can enter the encoding type.
    Example: utf-8, UTF-8-SIG

    -u - column_num. This is the column # that is being checked for whether it already exists in the table.
    It should be the unique identifier. This is used in determining whether to insert or upsert a record.
    Starts at 0.

"""

import argparse
import csv
import copy

from psycopg2.extensions import AsIs
from db_class import DB_Helper

from settings import logger

# Constants
VALID_SCHEMA = ['schema1', 'schema2', 'schema3']

# Dictionary of available sql statements to run.
sql = {}

# Need single quotes around the variables passed in for any comparison checks.
# If we're directly using column names or table names, do not need single quotes.

# Custom servers and warehouses.
sql['server_list1'] = """
select distinct server.id, server.name
from some_schema.some_table;
"""

sql['warehouses_list1'] = """
select wh.id, wh.db_name
from some_schema.some_table wh;
"""

sql['server_list2'] = """
select distinct server.id, server.name
from some_schema.some_table;
"""

sql['warehouses_list2'] = """
select dw.id, dw.db_name
from some_schema.some_table wh;
"""

sql['server_list_all'] = """
select distinct server.id, server.name
from some_schema.some_table;
"""

sql['warehouses_list_all'] = """
select dw.id, dw.db_name
from some_schema.some_table wh;
"""

# Returns a list of all tables that match the given input table.
# This is under a particular database.
sql['warehouse_tables'] = """
select table_schema, table_name
from information_schema.tables
where (table_schema = '{schema_check}')
and (table_type = 'BASE TABLE')
and (table_name = '{table_check}')
order by table_schema asc;
"""

# Returns a tuple of all available columns, for a given input table.
sql['column_list'] = """
select column_name
from information_schema.columns
where table_name = '{}'
"""

# Returns all values for a given column, for a given table.
sql['field_values_list'] = """
select {}
from {}
"""

# Return new record with all values, for a given table, where primary column identifier matches.
sql['new_value_list'] = """
select *
from {table_check}
where {field_name} = '{field_value}'
"""


def build_upsert_str(table_name, header_row, values_row, column_num):
    """
    Takes in the table_name, header_row, and values in: values_row, to build an upsert.
    Returns the sql statement as a string.
    """
    num_fields = len(header_row)
    primary_column_name = ''

    build_str = f"insert into {table_name} ("

    # Get the field names from the header_row.
    loop_count = 0
    for each_column in header_row:
        loop_count += 1
        if loop_count == num_fields:
            build_str += f"{each_column})"
        else:
            build_str += f"{each_column}, "

        if (loop_count - 1) == column_num:
            primary_column_name = f"{each_column}"

    if primary_column_name == '':
        logger.critical(f"Couldn't find the primary column name from column_num: {column_num} in table: {table_name}")
        exit(1)

    build_str += "values ('"

    # Get the values from the values_row.
    loop_count = 0
    for each_value in values_row:
        loop_count += 1
        if loop_count == num_fields:
            build_str += f"{each_value}')"
        else:
            build_str += f"{each_value}', '"

    build_str += f"on conflict ({primary_column_name}) do update set "

    # If there's a conflict, update all columns except for the primary column, which is column_num.
    loop_count = 0
    for each_value in values_row:
        loop_count += 1

        if (loop_count - 1) != column_num:

            if loop_count == num_fields:
                build_str += f"{header_row[loop_count - 1]} = '{each_value}'"
            else:
                build_str += f"{header_row[loop_count - 1]} = '{each_value}' , "

    return build_str


def build_insert_str(table_name, header_row, values_row):
    """
    Takes in the table_name, header_row, and values in: values_row, to build an insert.
    Returns the sql statement as a string.
    """
    num_fields = len(header_row)

    build_str = f"insert into {table_name} ("

    # Get the field names from the header_row.
    loop_count = 0
    for each_column in header_row:
        loop_count += 1
        if loop_count == num_fields:
            build_str += f"{each_column})"
        else:
            build_str += f"{each_column}, "

    build_str += "values ('"

    # Get the values from the values_row.
    loop_count = 0
    for each_value in values_row:
        loop_count += 1
        if loop_count == num_fields:
            build_str += f"{each_value}')"
        else:
            build_str += f"{each_value}', '"

    return build_str


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


def print_all_servers(server_list):
    """
    Print all servers available in a clean format.
    Assumes input is a list of servers, with each server having a list of: id followed by name.
    """
    my_server_str = 'server names: '
    for server in server_list:
        my_server_str += f'{server[1]}, '

    my_server_str = my_server_str.strip()
    my_server_str = my_server_str.rstrip(my_server_str[-1])
    logger.info(my_server_str)


def none_or_str(value):
    """
    Converts all string values of "None" to None.
    """
    if value == 'None':
        return None
    return value


def main(args):
    """
    Main procedure for scheduled run.
    """
    logger.main("Starting main procedure ...")

    action = args.action
    insert_type = args.type
    new_table_list = args.table.split('.')

    csv_name = args.csv_filename
    field_check1 = args.field
    value_check1 = args.value

    client_name = args.client
    encoding = args.encoding
    column_num = args.column_num

    if len(new_table_list) != 2:
        logger.critical("Need schema and table specified in the table parameter, separated by a period.")
        exit(1)

    my_schema = new_table_list[0]
    my_table = new_table_list[1]

    if my_schema not in VALID_SCHEMA:
        logger.critical(f"The schema provided is not a valid schema format. Valid formats: {VALID_SCHEMA}")
        exit(1)

    # data_list is a 2d list of the csv file.
    # The 1st index is the row #. The 2nd index is the column #.
    # The combination is the individual value.
    # Examples: data_list[0][0] = ['Value'] -- data_list[1][0] = '0123'
    data_list = []

    header_row = []

    # Check if parameters were passed correctly.
    if (csv_name is None) or (len(csv_name) == 0):
        if (field_check1 is None) or (value_check1 is None) or (len(field_check1) == 0) or (len(value_check1) == 0):
            logger.error("Program must have either the csv name filled out, or both field_check1 and value_check1 answered. Ending program.")
            exit(1)
        else:

            # Old method using field_check1 and value_check1
            # Check if there are multiple fields under field_check1, using a pipe delimiter.
            pipe_position = field_check1.find("|")

            # 1 field and 1 value.
            if pipe_position == -1:

                # Store the first field name and value.
                data_list.append(field_check1)
                data_list.append(value_check1)

                header_row = copy.deepcopy(data_list[0])

            # Multiple fields and values.
            else:
                # Pipe delimiters exist, so parse them out. Then add each of them to field_dictionary.
                # Assumes user entered an equal # of pipes between field_check1 and value_check1.
                field_list = field_check1.split("|")
                value_list = value_check1.split("|")

                header_row.append(field_list)

                # Store the header in the same format, using a csv file.
                data_list.append(field_list)
                data_list.append(value_list)

    else:
        # Open csv filename.
        with open(csv_name, mode='r', encoding=encoding) as f:
            csv_reader = csv.reader(f)

            for each_item in csv_reader:
                data_list.append(each_item)

        header_row = copy.deepcopy(data_list[0])

    logger.info(f"header_row: {header_row}")
    logger.info(f"1st row of data: {data_list[1]}")

    # Establish connection.
    connection_object = DB_Helper(host="some_host", database="some_database", user="some_user")
    logger.info(f"Connection to {connection_object} established.")

    # Get a list of all valid servers.
    if (client_name is None) or (len(client_name) == 0):
        valid_servers = connection_object.query(sql['server_list_all'], return_data=True)
    elif client_name == 'client1':
        valid_servers = connection_object.query(sql['server_list1'], return_data=True)
    elif client_name == 'client2':
        valid_servers = connection_object.query(sql['server_list2'], return_data=True)
    else:
        logger.critical('Invalid client name. Ending program.')
        exit(1)

    print_all_servers(valid_servers)

    # Count the # of checks and updates.
    num_servers_checked = 0
    num_tables_checked = 0
    num_updates = 0

    # Loop through all valid servers.
    for server in valid_servers:

        logger.info("")
        logger.main(f"server name: {server[1]}")

        # Get a list of valid all databases for this server.
        if (client_name is None) or (len(client_name) == 0):
            valid_warehouses = connection_object.query(sql['warehouses_list_all'].format(server[0]), return_data=True)
        elif client_name == 'client1':
            valid_warehouses = connection_object.query(sql['warehouses_list1'].format(server[0]), return_data=True)
        elif client_name == 'client2':
            valid_warehouses = connection_object.query(sql['warehouses_list2'].format(server[0]), return_data=True)
        else:
            logger.critical('Invalid client name. Ending program.')
            exit(1)

        logger.debug(valid_warehouses)

        # Loop through all valid databases.
        for warehouse in valid_warehouses:
            wh_connection = DB_Helper(host=server[1], database=warehouse[1], user="some_user")
            logger.main(f"Connected to database: {warehouse[1]}")

            # Check that the schema and table exists.
            total_tables = wh_connection.query(sql['warehouse_tables'].format(schema_check=my_schema, table_check=my_table), return_data=True)
            logger.debug(total_tables)

            num_tables = len(total_tables)
            if num_tables == 0:
                logger.info('Could not find a matching schema name / table name in this database.')
                continue

            combined_table = f'{my_schema}.{my_table}'
            logger.info(f"Found table: {combined_table}")

            try:

                column_tuples = wh_connection.query(sql['column_list'].format(AsIs(my_table)), return_data=True)

                # The queried column names come back as a list of tuples.
                # This gets the column names into a list.
                fixed_column_list = convert_tuples(column_tuples)

                # Check that every column in header_row is found in fixed_column_list.
                all_headers_found = True
                for each_header in header_row:
                    found_header = False
                    for each_column in fixed_column_list:
                        if str(each_header) == each_column:
                            found_header = True
                            break

                    if found_header == False:
                        logger.info(f"Couldn't find header: {each_header} in this table. Skipping this table.")
                        all_headers_found = False
                        break

                if all_headers_found == True:
                    logger.info("All headers found in this table.")
                    logger.info(f"table column names: {fixed_column_list}")

                    # Query all field values for the unique column # in header_row.
                    values_list_tuples = wh_connection.query(sql['field_values_list'].format(header_row[column_num], AsIs(combined_table)), return_data=True)
                    field_values_list = convert_tuples(values_list_tuples)

                    num_tables_checked += 1

                    # Loop through each_row in the data_list, excluding the header row.
                    row_count = 0
                    for each_row in data_list[1:]:

                        row_count += 1

                        # If each_row[column_num] already exists and we're doing an upsert --> continue.
                        # If each_row[column_num] does not exist --> continue.
                        if (each_row[column_num] in field_values_list and insert_type == 'upsert') or (each_row[column_num] not in field_values_list):

                            if len(field_values_list) <= 10:
                                logger.info(f"current field values: {field_values_list}")

                            # Build upsert statement and query it.
                            if insert_type == 'upsert':
                                upsert_query = build_upsert_str(AsIs(combined_table), header_row=header_row, values_row=each_row, column_num=column_num)
                                wh_connection.query(upsert_query)

                            # Build insert statement and query it.
                            elif insert_type == 'insert':
                                insert_query = build_insert_str(AsIs(combined_table), header_row=header_row, values_row=each_row)
                                wh_connection.query(insert_query)

                            num_updates += 1

                            # Print new field values for the primary column name.
                            names_tuples = wh_connection.query(sql['new_value_list'].format(table_check=combined_table, field_name=header_row[column_num], field_value=each_row[column_num]), return_data=True)
                            logger.info(f"row {row_count} -- {insert_type}ed value -- new record values: {convert_tuples(names_tuples)}")

                            if action == 'update':
                                wh_connection.commit()
                            elif action == 'rollback':
                                wh_connection.rollback()

            except Exception as e:
                wh_connection.close()
                logger.critical(f"Error: {e}")

        num_servers_checked += 1

    # Close the connection to connection_object.
    connection_object.close()
    logger.info("")
    if action == 'rollback':
        logger.main("Rolled back all updates.")
    logger.main(f"{num_updates} updates done out of {num_tables_checked} tables checked across {num_servers_checked} servers.")
    logger.main("Ending main procedure ...")


# Start Process.
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("-a", "--action", type=str, help="rollback or update", default="rollback", choices=["rollback", "update"], required=True)
    parser.add_argument("-y", "--type", type=str, help="insert type", choices=["insert", "upsert"], required=True)
    parser.add_argument("-t", "--table", type=str, help="enter table to view/update.", required=True)

    # Optional parameters
    parser.add_argument("-csv", "--csv_filename", type=none_or_str, help="the csv file to load.", default=None, required=False)
    parser.add_argument("-f", "--field", type=none_or_str, help="enter field1 to view/update.", default=None, required=False)
    parser.add_argument("-v", "--value", type=none_or_str, help="enter value1 to check/add.", default=None, required=False)
    parser.add_argument("-c", "--client", type=none_or_str, help="The client name to update custom warehouses.", default=None, required=False)

    parser.add_argument("-e", "--encoding", type=none_or_str, help="The encoding type of the csv file.", default='utf-8', required=False)
    parser.add_argument("-u", "--column_num", type=none_or_str, help="The column # checked for whether it already exists in the table.", default=0, required=False)

    global_args = parser.parse_args()

    main(global_args)
