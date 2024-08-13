# Standard library
import time
import random

# 3rd party library
import pyautogui

# Get current mouse x and y:
# print(pyautogui.position())
# Get current screen resolution width and height.
# print(pyautogui.size())
# pyautogui.typewrite("hello world")

int1 = input('Enter time in minutes:\n')
int1 = int(int1)

num_seconds = int1 * 60
num_seconds_per_cycle = 60
total_loops = int(round(num_seconds / num_seconds_per_cycle, 0)) * 2
num_loops_completed = 0

lower_range = num_seconds_per_cycle - 30
upper_range = num_seconds_per_cycle + 30

for i in range(total_loops):

    pyautogui.moveTo(918, 428, duration=0)
    print(f'Loading file. {num_seconds_per_cycle} sec per cycle. Progress {num_loops_completed} / {total_loops}')

    current_random_num = random.randint(lower_range, upper_range)
    millisecond_random_num = random.randint(0, 1000) / 1000

    total_wait = current_random_num + millisecond_random_num
    delta_wait = total_wait - 1

    random_tab_num = random.randint(1, 4)
    toggle_num = str(random_tab_num)

    pyautogui.keyDown('command')
    pyautogui.keyDown(toggle_num)
    time.sleep(1)
    pyautogui.keyUp('command')
    pyautogui.keyUp(toggle_num)

    # print(f'# of seconds to sleep: {total_wait} delta wait: {delta_wait}')

    time.sleep(delta_wait)
    num_loops_completed += 1
