

set_header_list = ['head1', 'head2', 'head3', 'head4']

schema = 'some_schema'
table_name = 'some_table'

csql = f"DROP TABLE IF EXISTS {schema}.{table_name}; CREATE TABLE {schema}.{table_name} ("

for h in set_header_list:
    print(csql)
    if h == set_header_list[-1]:
        csql += f"{h} TEXT"
    else:
        csql += f"{h} TEXT,"

csql+= ");"

print(csql)
print('')
