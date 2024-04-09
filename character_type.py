"""
Script to detect the character type of each character in a given string.
This helps you find out if theres any odd ascii characters that could throw a file load off.
"""


string1 = input('\nEnter the string of characters you want to check:\n')

for i in range(len(string1)):

    temp_str = f"character: {string1[i]}   ascii type: {ord(string1[i])}"
    if ord(string1[i]) == 32:
        temp_str += ' --> This is a normal space character'

    print(temp_str)
