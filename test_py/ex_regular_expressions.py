
import re

#each_header = '"some_column_name"'
each_header = 'some_column_name'

# Check that the column names begin with a letter or an underscore.
first_character = each_header[0]
print(re.findall("[a-zA-Z_]", first_character))
if re.findall("[a-zA-Z_]", first_character):
    print("This column name begins with a valid character.")
else:
    column_err_str = (f"Header: {each_header} does not begin with a letter or an underscore. This is an invalid column name.\n")
    column_err_str += ("Please check your header and try again.")
    print(f"{column_err_str}")

# Check that subsequent characters in the name are letters, numbers, or underscores.
if not re.match(r'^[a-zA-Z_0-9 ]+$', each_header):
    column_err_str = (f"Header: {each_header} contains characters that are not letters, numbers, or underscores. This is an invalid column\n")
    column_err_str += ("Please check your header and try again.")
    print(f"{column_err_str}")

