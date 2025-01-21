"""
Example of a generator function capturing an infinite data stream.
This one is the fibonacci sequence.
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
