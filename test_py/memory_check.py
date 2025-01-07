from pympler import asizeof

number_to_check = 2489787
my_list = [i for i in range(number_to_check)]
total_size = asizeof.asizeof(my_list)

print(f"Total memory size: {total_size:,} bytes")
