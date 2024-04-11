"""
Create folders for a new project.
"""

import os

q1_string = '\nWhat is the name of this project?\n'
ans1 = input(q1_string)

path1 = '/Users/some_user/Desktop/Work/'
full_path = path1 + ans1
os.mkdir(full_path)

sub_folder_list = ['original', 'supporting-docs', 'load']
for each_folder in sub_folder_list:
    os.mkdir(full_path + '/' + each_folder)
