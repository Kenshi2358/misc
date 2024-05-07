
# import datetime
# now = datetime.datetime.now()
# print(f'\nYear: {now.strftime("%Y")}')
# print(f'Month: {now.strftime("%m")}')
# print(f'Month: {now.strftime("%b")}\n')

# from datetime import date, timedelta
# prev = date.today().replace(day=1) - timedelta(days=1)
# print (prev.month)

# =====================================================
# Slicing / Slice Examples.

# my_name = 'John Smith'
# space_positiion = my_name.find(' ')

# print(my_name[:space_positiion])
# print(my_name[space_positiion + 1:])

# Check the last character.
#print(my_name[-1])
# Look at all characters, but the last character.
# print(my_name[:-1])

# To get the last 4 characters:
#print(my_name[-4:])

# To get all characters after the first 3 characters:
#print(my_name[3:])
# pos = 7
# print(my_name[0:pos])

# print(my_name[0:4])
# some_position = 4
# print(my_name[0:some_position])
# Return the last item in a splitted list.
#print(my_name.split(' ')[-1])

# output1 = 'folder1/folder2/'
# first_forward_slash = output1.find('/')
# s3_bucket = output1[0:(first_forward_slash + 1)]
# s3_key = output1[(first_forward_slash + 1):]

# print(s3_bucket)
# print(s3_key)


# =====================================================
#a, b = 5, 4
# if (a == 5) and (b == 4):
#     print('a regular if statement.')

# if (a == 5) \
# and (b == 4):
#     print('using sorcery.')

# if ((a == 5)
# and (b == 4)):
#     print('using parentheses.')

# # Using a boolean operator to break to a new line.
# # and, or, not --> are all boolean operators.
# if (a == 5 and 
#        b == 4):
#     print('a regular if statement.')


# filename_list = ['a', 'b', 'c']
# for x in filename_list:
#     print(x)

# =====================================================
# import os
# import fnmatch
# import logging

# # Set log configuration.
# logging.basicConfig(
#     format='%(asctime)s %(levelname)-8s %(message)s',
#     level=logging.INFO,
#     datefmt='%Y-%m-%d %H:%M:%S'
# )

# path1 = '/Users/some_user/Desktop/folder1/'
# file_pattern = '*.py'
# for each_file in os.listdir(path1):
#     if os.path.isfile(os.path.join(path1, each_file)):
#         if fnmatch.fnmatch(each_file, file_pattern):
#             logging.info(each_file)

# =====================================================
# Global scope example:
def addition(a, b):
    global x
    print(x)
    x += 1
    return a + b

if __name__ == "__main__":
    x = 100
    c = addition(a=3, b=5)
    print(x)

# =========================================
# Local scope example:
def check_y():
    y = 2
    print(f"value of y inside function is: {y}")

y = 1
check_y()
print(f"value of y outside function is: {y}")

# Check all local variables example:
def demo1():
    print("Here no local variable  is present : ", locals())

def demo2():
    name = "John"
    print("Here local variables are present : ", locals())

demo1()
demo2()

# =====================================================
# Example using eval function.
# Eval evalutes the specified expression.
# some_text = '12345'
# my_var = eval('some_text')
# print(my_var)

# =====================================================
# Different ways to concatenate.
# new_name = "Rambo"
# year = "2022"
# new_name = new_name + str(year)
# new_name = f'{new_name}_{year}'
# print(new_name)

# =====================================================
# Python String join() method example.
# my_list = ['Python', 'is', 'cool']
# print(' '.join(my_list))

# =====================================================

# my_str = 'Scott'
# variable_type = type(my_str)
# if variable_type is str:
#     print('This is a string')
# elif variable_type is dict:
#     print('This is a dictionary')
# =====================================================
# Fnmatch check - case sensitivity:

# import fnmatch
# if fnmatch.fnmatch(".TXT", '*.txt'):
#     print('not case sensitive')
# elif fnmatch.fnmatch('.txt', '*.txt'):
#     print('case sensitive')

# x = round(5/2, 0)
# print(int(x))

# =====================================================
# Datetime example for RFC 3339 format:

# import datetime
# current_date = datetime.datetime.now(datetime.timezone.utc).isoformat()
# mod_date = '2022-06-29T11:21:28.665Z'

# #print(current_date)
# print(mod_date)
# d = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=15)).isoformat()
# print(d)

# if mod_date >= d:
#     print('mod date was modified in the last 15 days')
# else:
#     print('mod date was not modified in the last 15 days')
# =====================================================

