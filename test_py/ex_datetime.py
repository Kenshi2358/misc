import datetime
import time

def date_time(datetime_format="%Y-%m-%d_%H-%M-%S"):
    return time.strftime(datetime_format)

dir_time = date_time(datetime_format="%Y-%m-%d_%H-%M-%S")
print(dir_time)
