# !/usr/bin/python
from datetime import datetime
import time
import logging
import os

from sys import argv


def remove_ds(string):
    """
    Removes double spaces.
    """
    return string.replace("  ", " ")


def clean_str(curr_str):
    """
    Converts the expression to string.
    Remove double spaces. Remove spaces at each end.
    """

    curr_str = str(curr_str)
    curr_str = remove_ds(curr_str)
    curr_str = curr_str.strip()
    return curr_str


# my_string = " John Smith "
# my_string = clean_str(my_string)
# print(my_string)
# print('')

# The first item in argv is the name of the Python script you're running.
# Any additional arguments are arguments passed to this script.
# This will only be shown when you run this script from terminal, with:
# python3 z_notes2.py test2
# Here script will be z_notes2.py     and argument1 will be test2
# if len(argv) == 2:
#     script, argument1 = argv
#     print(f'script {script} argument1 {argument1}')


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
	level=logging.INFO,
	datefmt='%Y-%m-%d %H:%M:%S'
)

# sleep = 1
# now = datetime.now()
# print(now)
# # %s allows you to insert a string.
# logging.info("Sleeping job for %s - %s" % (sleep,now))
# logging.info(f"Sleeping job for {sleep} - {now}")
# time.sleep(sleep)

# If you're using ints, use %d instead.
# %d - integer.
# %s - string.
# #f - floating point numbers.

# Tab and # Shift-Tab to move text over or back 1 tab.

# =========================================
# Python program to understand about locals
# here no local variable is present

# def demo1():
#     print("Here no local variable  is present : ", locals())

# # here local variables are present
# def demo2():
#     name = "Someones_name"
#     print("Here local variables are present : ", locals())

# # driver code
# demo1()
# demo2()

# =========================
# Split function returns a list. The length of the list depends on the delimiter.
# length could be 1 or 5.
# my_string = 'mdx_taxa.datum_category_code'
# new_table_list = my_string.split('.')

# my_schema, my_table = '', ''
# for each_name in new_table_list:
#     my_schema = new_table_list[0]
#     my_table = new_table_list[1]

# =========================
# print(f'my_schema: {my_schema}   my_table: {my_table}')

# datum_category_list = ["name", "Unknown"]
# datum_category_name_value = ''
# datum_category_name_field = ''
# for count, value in enumerate(datum_category_list):
#     if count == 0:
#         datum_category_name_field = datum_category_list[0]
#     elif count == 1:
#         datum_category_name_value = datum_category_list[1]
# print(f'datum_category_name_value: {datum_category_name_value}   datum_category_name_field: {datum_category_name_field}')

# =========================
# Learn os and time modules.

#cwd = os.getcwd()
#print(f"Current working directory {cwd}")

#timestamp = int(time.time())
#print(f"timestamp: {timestamp}")

# Open file
# fd = os.open("f1.txt",os.O_RDWR|os.CREAT)

# # Writing text
# ret = os.write(fd,"This is test")

# # ret consists of number of bytes written to f1.txt
# print("the number of bytes written: ")
# print(ret)

# print("written successfully")

# # Close opened file
# os.close(fd)
# print("Closed the file successfully!!")
# =========================

# If you want a break statement in a location that doesn't have breaks,
# you can add a dummy for loop, like this.
# for _ in (True,):
#     print('hello')
#    break

from zipfile import ZipFile

full_file_path = '/Users/some_user/Desktop/Work/some_folder/zip1.zip'
current_file = 'zip1.zip'

last_4_characters = current_file[-4:]
if last_4_characters == '.zip':

    print(f"unzipping {current_file}")

    list_of_files = ''

    with ZipFile(full_file_path, 'r') as zip_object:

        list_of_files = zip_object.namelist()

        # Loop through all files and extract all files, excluding __MACOSX.
        for each_file in list_of_files:

            if each_file.find("__MACOSX") == -1:
                print(f"extracting {each_file}")
                zip_object.extract(each_file, path='/Users/some_user/Desktop/folder1/')

    print(f"list of archived files: {list_of_files}")
