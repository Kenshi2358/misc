import datetime
from datetime import timedelta
import time

def date_time(datetime_format="%Y-%m-%d_%H-%M-%S"):
    return time.strftime(datetime_format)

# Get current formatted time.
dir_time = date_time(datetime_format="%Y-%m-%d_%H-%M-%S")
print(dir_time)

# Get yesterday formatted time.
yesterday = datetime.date.today() - datetime.timedelta(days=1)
yesterday_formatted = yesterday.strftime("%b %d")
print(f"Yesterday's date was: {yesterday_formatted}")

# Get weekend formatted time.
weekend = datetime.date.today() - datetime.timedelta(days=3)
weekend_formatted = weekend.strftime("%b %d")
print(f"The start of the weekend was: {weekend_formatted}")

# Get day of the week.
print(f"Today is: {datetime.date.today().strftime("%A")}")

pass
