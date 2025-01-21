"""
Example of a generator function capturing an infinite data stream.
This one is the fibonacci sequence.

Generators return an iterator object (or generator object that supports the iterator protocol).
Instead of using a return to send back a single value,
generator functions use yield to produce a series of results over time.
This allows the function to generate values and pause it's execution after each yield,
maintaining it's state between iterations.

yield provides a sequence of values over time.
"""

def fib():
    a = 0
    b = 1
    while True:
        yield a
        temp_a = a
        a = b
        b = temp_a + b

# output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
i = 0
for result in fib():
    print(f"result: {result}")
    i += 1
    if i >= 10:
        break
