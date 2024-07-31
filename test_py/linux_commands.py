"""
This script shows the different options to run a linux command in Python.

There are 3 options:
1) subprocess.Popen --> issues: lengthy steps for each query.
Have to enter .communicate method so script waits for execution to finish.

2) subprocess.run --> issues: better than Popen, but only works on Python 3.7

3) os.system() --> issues: does not allow you to return output.
Otherwise, this is the best option.

Options to run sql commands:
1) psycopg2 --> Requires connecting to db_helper.py from des-utilities.

"""
# Standard library imports
import subprocess
import os

dir1 = "/Users/shahnert/Desktop/Repos/misc"
ls_results = subprocess.check_output(['ls', dir1]).decode().split()

for each_str in ls_results:
    print(each_str)

print('')
os.system('echo "Hello World"')
print('')

