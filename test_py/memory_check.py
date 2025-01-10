from pympler import asizeof

number_to_check = 300_000
my_list = [f"{i}I'm a dog. My name is Logan. Bark bark. I love to eat and go for runs." for i in range(number_to_check)]
total_size = asizeof.asizeof(my_list)

print(f"Total memory size: {total_size:,} bytes")
