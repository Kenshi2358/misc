# When you have a very long list and that list doesn't need to be updated,
# you should use a hash table instead. Python dictionaries and sets are hash tables.
# For lists specifically: you can use sets instead.
# Note that sets are unchangeable.

import time
import random

def solution1(A, B):
    for i in range(len(A)):
        if A[i] not in B:
            return A[i]

def solution2(A, B):
    H=set(B)
    for i in range(len(A)):
        if A[i] not in H:
            return A[i] 

L = list(range(0, 100000))
L[-3] = -random.randint(0,100000)
R = list(range(0, 100000))

start_time = time.time()
solution1(L, R)
end_time = time.time()

# Takes approximately 28 seconds.
print(f"solution 1: time in seconds: {round(end_time - start_time, 4)}")

start_time=time.time()
solution2(L, R)
end_time = time.time()

# Takes approximately 0.0048 seconds.
print(f"solution 2: time in seconds: {round(end_time - start_time, 4)}")
