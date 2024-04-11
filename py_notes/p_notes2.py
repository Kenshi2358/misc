# __name__ is a built-in variable which evaluates to the name of the current module. However, if a module is being run directly (as in myscript.py above), then __name__ instead is set to the string "__main__". Thus, you can test whether your script is being run directly or being imported by using __name__.

# It's boilerplate code that protects users from accidentally invoking the script when they didn't intend to.

'''if __name__ == "__main__":
    print('hello')
    exit(0)
'''

# When a script uses a line like this, the # __file__ means:
# When a module is loaded from a file in Python, __file__ is set to its path.
# You can then use that with other functions to find the directory that the file is located in.

# mrf = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

# user_ans = input('\n0 or 1?\n')
# user_ans = int(user_ans)
# if user_ans == 0:
#     # exit(0): a clean exit without any errors or problems.
#     exit(0)
# elif user_ans == 1:
#     # exit(1): There was some issue / error / problem and that is why the program is exiting.
#     exit(1)

'''
The # in the exit command determines the exit status of the program when it finishes
0 for success, 1 for error, generally.

This is not unique to python.
On many systems, exit(1) signals some sort of failure.
The number you pass to the exit() function is simply your program's return code, which is given to the operating system.
'''


# ===================================
'''Map function in python:
map() - function returns a map object of the results after applying
the given function to each item of a given iterable (list, tuple etc.)

Syntax: map(fun, iter)

Parameters:
fun: It is a function to which map passes each element of the given iterable.
iter: It is an iterable which is to be mapped.
'''
# # Simple example:
# def addition(n):
#     return n + n

# # Double all numbers using map()
# numbers = [1, 2, 3, 4]
# result = map(addition, numbers)
# print(list(result))

# When using the .strip method with map, you cannot use parentheses.
# my_list = ['  cats', 'dogs ', ' fish ', ' mice ']
# result = map(str.strip, my_list)
# print(list(result))

# Example of how to work with a list of a list.
# blah = [['datum_category_code'], ['name'], ['description'], ['section_name']]
# for x in blah:
#     for y in x:
#         print(y)


# ===================================
# Logging Examples
#import logging
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

#logging.warning('Watch out!')  # will print a message to the console
#logging.info('I told you so')  # will not print anything

# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# ===================================
# List comprehension example:
# Old way: Iterate through a string using a for loop.
# h_letters = []
# for letter in 'human':
#     h_letters.append(letter)
# print(h_letters)

# h_letters = [letter for letter in 'human']
# print(h_letters)

# # Syntax: [expression for item in list]

# # Same List Comprehension using the Lambda function.
# letters = list(map(lambda x: x, 'human'))
# print(letters)

# Expression definition - any statement that may be evaluated to determine its value.
# Examples:
# 2 + 3
# y + 6
# True

# ===================================
# Lamba Functions - small anonymous functions. Can take any # of arguments, but can only have one expression.
# Syntax:
# lambda arguments: expression

# Good example.
# def multiplier(n):
#     print(f'the n variable is: {n}')
#     return lambda a: a * n

# #my_doubler is of data type: function with a passed in value of 2.
# my_doubler = multiplier(2)
# my_tripler = multiplier(3)
# print(my_doubler(10), my_tripler(10))

# Poor example.
# x = lambda a: a + 10
# print(x(5))
# ===================================
# Filter Function
# Syntax:
# filter(function, iterable)

# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# # Here adults is a class data type.
# adults = filter(myFunc, ages)
# for x in adults:
#   print(x)
# ===================================
# Making a dictionary of variable names and initializing them all to empty string.

name_dictionary = {}
type_list = ['field_id', 'field_description', 'field_is_primary']

for i in range(1, 4):
    for each_type in type_list:
        name_var = f'{each_type}{i}'
        name_dictionary[name_var] = ""

print(name_dictionary)

for k in range(3):
    for each_type in type_list:
        name_var = f'{each_type}{k+1}'

        if each_type.find('field_id') >= 0:
            name_dictionary[name_var] = 'some_id'
        elif each_type.find('field_description') >= 0:
            name_dictionary[name_var] = 'some_description'
        elif each_type.find('field_is_primary') >= 0:
            name_dictionary[name_var] = 'some_primary'

print(name_dictionary)
print('done')

# ===================================


