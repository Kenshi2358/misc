
import random

#num_loops = random.randint(10, 12)
num_loops = 10

for i in range(num_loops):
    current_str = "Hello World"
    new_str = ''

    for k in range(len(current_str)):
        random_bits = bool(random.getrandbits(1))
        if random_bits:
            new_str += current_str[k].upper()
        else:
            new_str += current_str[k].lower()

    print(new_str)
