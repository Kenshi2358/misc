"""
Example showing how to use psycopg to update a sql table.
The fields being updated with a variable require single quotes around them.

The script will not actually work, as all credentials have been removed.
"""

import psycopg
import datetime

server = "some_server"
database = "some_database"

sql = {}

status = "success"
todays_date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
error_msg = "sample error msg"

sql['update_status'] = f"""
update schema_name.table_name
set status = '{status}', modified = '{todays_date}', error_msg = '{error_msg}'
where job_name = 'my_job_name';
"""

conn = psycopg.connect(host=server, dbname=database, user="username1")
cursor = conn.cursor()

cursor.execute(sql['update_status'])
conn.commit()

print("Ran sql query")
