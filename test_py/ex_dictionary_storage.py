"""
Example of updating a dictionary through:
a) direct assignment
b) update method.

Either method works.
"""

my_dict = {}
#my_dict["height"] = 64
print(my_dict)

if "height" in my_dict:
    my_dict["height"] = my_dict["height"] + 64
else:
    my_dict["height"] = 64

print(my_dict)

my_dict.update({"height": my_dict["height"] + 64})
print(my_dict)
