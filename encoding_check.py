"""
This script checks the encoding type of a file.
This is helpful when troubleshooting a file with bad unicode / ascii characters.

chardet.detect returns a dictionary providing the encoding of the file.
The key is: 'encoding' with value: 'encoding type'.

Some common file encoding types are:
UTF-8, UTF-16, Windows-1252, ascii

Usage:
    python file_encoding_check.py -f "my_path_and_filename"

"""

import chardet
import argparse

parser = argparse.ArgumentParser()

# Required parameters.
parser.add_argument('-f', '--filename', help='the path and filename to check', required=True)

args = parser.parse_args()


print("Starting file encoding check ...")

rawdata = open(args.filename, "rb").read()
results = chardet.detect(rawdata)
charenc = results['encoding']

print(f"File encoding type: {charenc}")

print("Done running file encoding check ...")
