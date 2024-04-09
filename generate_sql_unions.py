
schema_name = input('Enter the schema_name:\n')
table_name = input('Enter the table name:\n')
column_name = input('Enter the column_name:\n')

num_iterations = 10
sql = ""
for i in range(1, num_iterations + 1, 1):
    if i != 1:
        sql += "\nunion\n"
    sql += f"""
    select distinct {column_name}_{i}
    from {schema_name}.{table_name}
    where {column_name}_{i} is not null
    """
sql += ";"

print(sql)
pass
