
import re

each_header = "first_name"
#each_header = '5first_name#$#$%'

# Check that the column name begins with a letter or an underscore.
first_character = each_header[0]

if re.findall("[a-zA-Z_]", first_character):
    print(f"\nHeader: {each_header} begins with a valid character, which is: {first_character}")
else:
    column_err = f"\nHeader: {each_header} does not begin with a letter or an underscore."
    column_err += "\nThis is an invalid column name.\n"
    column_err += "Please check your header and try again."
    print(f"{column_err}")

# Check that subsequent characters in the name are letters, numbers, or underscores.
if not re.match(r'^[a-zA-Z_0-9 ]+$', each_header):
    column_err = f"\nHeader: {each_header} contains characters that are not letters, numbers, or underscores."
    column_err += "\nThis is an invalid column name.\n"
    column_err += "Please check your header and try again."
    print(f"{column_err}")
