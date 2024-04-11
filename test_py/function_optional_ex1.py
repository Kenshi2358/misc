
def adding_one(a, b, c='5'):
    a += 1
    b += 1

    return a, b, c

input_a = 10
input_b = 20
results = adding_one(input_a, input_b)

print(f"After adding one to a and b, we have a: {results[0]} b: {results[1]}")
print(f"We also returned the optional parameter c: {results[2]}")
