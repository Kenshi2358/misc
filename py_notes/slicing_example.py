# Slicing Examples.

my_name = 'John Smith'
space_positiion = my_name.find(' ')

print(my_name[:space_positiion])
print(my_name[space_positiion + 1:])

# Check the last character.
print(my_name[-1])
# Look at all characters, but the last character.
print(my_name[:-1])

# To get the last 4 characters:
print(my_name[-4:])

# To get all characters after the first 3 characters:
print(my_name[3:])
pos = 7
print(my_name[0:pos])

print(my_name[0:4])
some_position = 4
print(my_name[0:some_position])

# Return the last item in a splitted list.
print(my_name.split(' ')[-1])

output1 = 'folder1/folder2/'
first_forward_slash = output1.find('/')
s3_bucket = output1[0:(first_forward_slash + 1)]
s3_key = output1[(first_forward_slash + 1):]

print(s3_bucket)
print(s3_key)
pass
