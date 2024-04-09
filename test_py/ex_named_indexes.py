
# Dictionary of available sql statements to run.
sql = {}

sql['insert_datum'] = """
insert into {table_name} ({column1}, {column2})
values ('{value1}', '{value2}')
"""

my_current_string = sql['insert_datum'].format(table_name='blah1', column1='blah2', column2='blah3', value1='blah4', value2='blah5')
print(my_current_string)
