def some_function(a, b, c):
    a += 1
    b += 1
    c -= 1

    d = {}
    d["color"] = "red"
    return a, b, c, d

a, b, c, d = some_function(5, 10, 20)

print(a)
print(b)
print(c)
print(d)
