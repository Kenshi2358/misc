"""
Example of how to write to a text file.
"""

apd = {
'address': 0,
'city': 0,
'line1': 0
}

# for each_keyword in apd:
#     print(each_keyword)
#     print(apd[each_keyword])

# =======================================
line1 = 'Now the file has more content!'

with open('ex_file_writing1.txt', 'w') as f:
    f.write(line1)
    f.write('\n')
    f.write(str(apd))
