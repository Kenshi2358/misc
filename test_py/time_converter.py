import math

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


seconds = 123.111212123
result = convert_time(seconds)
print(result)

