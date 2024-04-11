# Learning structural pattern matching with Python 3.10
# Example:

# def http_error(my_status):
#     match my_status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "status 418"
#         case _:
#             return "Something's wrong with the internet"

# # If the wildcard case match: case _: doesn't exist and we hit that scenario,
# # A no-op occurs and prints None.
# status = 450
# print(http_error(status))

user = 'john_smith'
member_since = '2018'

print(f'{user}')
print(f'{user=}')

print(f'{member_since}')
print(f'{member_since=}')


# =====================================================
# := allows for assign of variables within expressions.
# Example:

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# if (n := len(a)) > 10:
#     print(f"List is too long ({n} elements, expected <= 10)")
# else:
#     print(f'else statement. Value of n: {n}')
# print(n)

# Negative infinity example.
#if -500 > -float('inf'):
#    print(-float('inf'))


# =====================================================
# Example using the built-in function: breakpoint.

# my_name = 'Scott'
# # Create a loop over 6 integers
# for i in range(6):

#     print(i, my_name)

#     if i == 1:
#         import pdb; pdb.set_trace()

#     # Create breakpoint at # 3
#     if i == 3:
#         breakpoint()

# =====================================================
# Print the working directory using os module.
# import os
# pwd = os.path.dirname(os.path.realpath(__file__))
# print(pwd)

# =====================================================
# Example of list not callable error
# when overriding reserved class list to a new object.

# list = [5, 65, 72, 81, 106, 131,
#         136, 147, 151, 176, 186,
#         187, 188, 189, 190, 206,
#         286, 343]


# def Convert(string):
#     """
#     Converts string to list, with a space delimiter.
#     """
#     li = list(string.split(" "))
#     return li

# str1 = "The quick brown fox jumped over the lazy cat"
# print(Convert(str1))
# =====================================================
# Count the # of occurrences of a specific character in a string.
# my_str1 = 'first_name last_name'

# num_count = my_str1.count('t')
# print(f'there are {num_count} t characters')

# num_count = my_str1.count('e')
# print(f'there are {num_count} e characters')

# =====================================================
