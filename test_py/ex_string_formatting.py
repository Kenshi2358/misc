
# name = 'Scott'
# pet = 'dog'

# Oldest method: %-formatting.
print('My name is %s and I like to walk my %s.' %(name, pet))

# Newer method: string formatting.
print('My name is {} and I like to walk my {}.'.format(name, pet))
# string formatting using named indexes.
print('My name is {current_name} and I like to walk my {current_pet}.'.format(current_name=name, current_pet=pet))

# Newest method: f-string example.
print(f'My name is {name} and I like to walk my {pet}.')


# Example of using the split method.
table_name1 = 'public.table_name1'
table_name2 = 'table_name2'

table_items1 = table_name1.split('.')
table_items2 = table_name2.split('.')
