#!/usr/bin/env python

# ======================================================
# Example of using the string format() method in Python with empty placeholders.

#my_dogs_name = 'Logan'
#print('some string with variable {}'.format(my_dogs_name))

# ======================================================
# Placeholders can be identified using named indexes: {price}, 
# numbered indexes {0}, or empty placeholders {}.

# Using named indexes is 10x better than empty placeholders where you have to get order right.
# text1 = "My name is {fname}, I'm {age} years old".format(fname = "Scott", age = 300)
# print(text1)

# text2 = "My name is {fname}, I'm {age} years old".format(age = 300, fname = "Scott")
# print(text2)

# ====================================

# for i in range(5, 11):
#     print(i)

# Lists:
# fruit_list = ['Apples', 'Oranges', 'Strawberries']


# An f-string is a string literal.
# for each_fruit in fruit_list:
#     print(f'This fruit is named: {each_fruit}');

# if each_fruit[0] == 'Apples':
#     print('yes this is an apple.')
# else:
#     print('no this is not an apple.')

# a, b = [], []
# print(a)
# print(b)
# print(type(a))

# my_list1 = []
# my_list1.append('World Cup')
# print(my_list1)

my_dictionary = {}
my_dictionary["color"] = "red"
my_dictionary["pet"] = "dog"

my_dictionary['house'] = 'big'
#print(my_dictionary)
my_dictionary['client'] = {"1": "select count(*) from schema_name.table_name"}

for each_key, each_value in my_dictionary.items():
    print(each_key)
    print(each_value)

pass

#print('hello', 'world', 'cat', 'dog')

# =======================================
# Relative imports

# Examples:
# from .some_module import some_class
# from ..some_package import some_function
# from . import some_class

# Relative imports make use of dot notation to specify location.

# A single dot means that the module or package referenced is in the same directory as the current location. Two dots mean that it is in the parent directory of the current location—that is, the directory above. Three dots mean that it is in the grandparent directory, and so on.

# =======================================
# Example:
# Given a list of strings containing backslashes and other characters
# - Remove backslashes.
# - Remove tabs and carriage returns.
# - Convert double quotes to single quotes.

scrubbed_list = [r'{"Building Name \/*\\"}', r'"De\"Name"']

print(f'\n{scrubbed_list}\n')

# replace \\ with \\\\
# remove 0x09
# remove 0x0a
# replace double quotes with single quotes
replace_dictionary = {    
    r"\\": r"\\\\",    
    r"\t": "",
    r"\n": "",
    r'\"': r"'"
}

for each_scrub in scrubbed_list:
    for key, value in replace_dictionary.items():
        if key in each_scrub:

            each_scrub = each_scrub.replace(key, value)
    
    print(f'{each_scrub}\n')
    pass

# =======================================
# Example: Finding character position.

name1 = 'Meowly Mc\"meowmeow'
space_pos = name1.find(' ')
print(space_pos)
o_pos = name1.find('o')
print(o_pos)
last_name_pos = name1.find('Mc')
print(last_name_pos)

char_set_pos = name1.find('\"')
print(char_set_pos)

new_str = name1[(char_set_pos + 1):(char_set_pos + 2)]
print(new_str)
print(name1.isalpha())
