# Standard library
import time
import random

# 3rd party library
import pyautogui

# Get current mouse x and y:
# print(pyautogui.position())
# To type text:
# pyautogui.typewrite("hello world")

int1 = input('Enter time:\n')
int1 = int(int1)

num_seconds = int1 * 60
num_seconds_per_cycle = 60
total_loops = int(round(num_seconds / num_seconds_per_cycle, 0)) * 2
num_loops_completed = 0

# Get the width and height dimensions.
max_size = pyautogui.size()

# Get the second ranges.
max_delta_seconds = 30
lower_range = num_seconds_per_cycle - max_delta_seconds
upper_range = num_seconds_per_cycle + max_delta_seconds

# Get the second press down ranges.
max_ctrl_down = 0.5
ctrl_down_lower = 1 - max_ctrl_down
ctrl_down_upper = 1 + max_ctrl_down

# Get the pixel ranges.
max_delta_pixels = 100
base_x = 918
base_y = 428
lower_x_range = base_x - max_delta_pixels
upper_x_range = base_x + max_delta_pixels

lower_y_range = base_y - max_delta_pixels
upper_y_range = base_y + max_delta_pixels

# Get the duration ranges.
base_duration = 0.2
max_delta_duration = 0.1
duration_lower = base_duration - max_delta_duration
duration_upper = base_duration + max_delta_duration


for i in range(total_loops):

    delta_rand_x = random.randint(lower_x_range, upper_x_range)
    delta_rand_y = random.randint(lower_y_range, upper_y_range)

    duration_lower_int = round(duration_lower * 1000)
    duration_upper_int = round(duration_upper * 1000)
    delta_rand_duration = random.randint(duration_lower_int, duration_upper_int)
    delta_rand_duration_ms = delta_rand_duration / 1000

    pyautogui.moveTo(delta_rand_x, delta_rand_y, duration=delta_rand_duration_ms)
    print(f'Loading file. {num_seconds_per_cycle} sec per cycle. Progress {num_loops_completed} / {total_loops}')

    current_random_num = random.randint(lower_range, upper_range)
    millisecond_random_num = random.randint(0, 1000) / 1000

    total_wait = current_random_num + millisecond_random_num
    delta_wait = total_wait - 1

    random_tab_num = random.randint(1, 4)
    toggle_num = str(random_tab_num)

    ctrl_down_lower_int = round(ctrl_down_lower * 10)
    ctrl_down_upper_int = round(ctrl_down_upper * 10)
    ctrl_down_time = random.randint(ctrl_down_lower_int, ctrl_down_upper_int)
    ctrl_down_time_ms = ctrl_down_time / 10

    pyautogui.keyDown('command')
    pyautogui.keyDown(toggle_num)
    time.sleep(ctrl_down_time_ms)
    pyautogui.keyUp('command')
    pyautogui.keyUp(toggle_num)

    # print(f'# of seconds to sleep: {total_wait} delta wait: {delta_wait}')

    time.sleep(delta_wait)
    num_loops_completed += 1
