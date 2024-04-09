from datetime import datetime
import pytz

aware_us_east = datetime.now(pytz.timezone('US/Eastern'))
aware_paris = datetime.now(pytz.timezone('Europe/Paris'))

print(f"The US Eastern time is: {aware_us_east}")
print(f"The time in Paris, France is: {aware_paris}")

