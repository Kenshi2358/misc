import sys
from pympler import asizeof


def convert_bytes(bytes, units=['bytes', 'KB', 'MB', 'GB', 'TB']):
    """
    returns a human readable string representation of bytes
    """
    if bytes < 1024:
        return f"{bytes:.2f} {units[0]}"
    else:
        return convert_bytes((bytes/1024.0 * 1.0), units[1:])


number_to_check = 300_000
my_list = [f"{i}I'm a dog. My name is Logan. Bark bark. I love to eat and go for runs." for i in range(number_to_check)]
total_size = asizeof.asizeof(my_list)

bytes_str = convert_bytes(total_size)
print(f"Total memory size: {total_size:,} bytes, which is {bytes_str}")

total_size_2 = sys.getsizeof(my_list)
bytes_str_2 = convert_bytes(total_size_2)
print(f"Total memory size (per sys): {total_size_2:,} bytes, which is {bytes_str_2}")