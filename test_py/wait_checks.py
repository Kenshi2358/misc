
import time

total_checks = 20
current_minute = 0

for check_num in range(1, total_checks + 1, 1):

    if check_num <= 10:
        current_minute += 1
        print(f"Waiting 1 sec before checking endpoint - Second # {current_minute}")
        time.sleep(1)
    else:
        current_minute += 5
        print(f"Waiting 5 secs before checking endpoint - Second # {current_minute}")
        time.sleep(5)