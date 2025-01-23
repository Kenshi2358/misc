import os

file_list = ['file1.txt', 'file2.txt']
local_path = '/Users/shahnert/Downloads'
# local_path = ''

for each_file in file_list:
    full_file_path = os.path.join(local_path, each_file)
    print(full_file_path)
    pass

pass
