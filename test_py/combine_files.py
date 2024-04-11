import os
import glob

path = '/Users/some_username/Desktop/folder1/'
output_path = '/Users/some_username/Desktop/folder1/csv_output/'

file_list = os.listdir(path)

with open(output_path + "combined_csv.csv", "w") as outfile:

    for each_file in file_list:
        with open(path + each_file, 'r') as infile:
            outfile.write(infile.read())
