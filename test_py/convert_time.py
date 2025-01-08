import math
from time import sleep, time

def convert_time(total_seconds) -> str:

    output_str = ''
    minutes = 0

    if total_seconds >= 60:
        minutes = math.floor(total_seconds / 60)
        num_seconds = total_seconds % 60
    else:
        num_seconds = total_seconds

    if minutes == 0:
        output_str += f"{num_seconds:2.2f} sec"
    else:
        output_str += f"{minutes:2} min {num_seconds:2.2f} sec"

    return output_str

time_start = time()
sleep(1.579)
time_end = time()
net_time = time_end - time_start

result = convert_time(net_time)
print(result)
pass
