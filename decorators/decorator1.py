
# This is a decorator. This is also a wrapper.
# Wrapper and decorator mean the same thing.

def positive_input(func):
    def check_negative(x):
        if x <= 0:
            raise ValueError("Input must be positive")
        return func(x)
    return check_negative

@positive_input
def square(x):
    return x**2

@positive_input
def add_one(x):
    return x + 1

@positive_input
def add_two(x):
    return x + 2

print(square(5))
print(add_one(5))
print(add_two(5))

print(add_two(-10))

pass

