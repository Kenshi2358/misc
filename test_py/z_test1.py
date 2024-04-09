import time
import pyautogui
import random

# Get current mouse x and y:
#print(pyautogui.position())
# Get current screen resolution width and height --> 1920, 1080.
#print(pyautogui.size())
#pyautogui.typewrite("hello world")

int1 = input('Enter time in minutes:\n')
int1 = int(int1)

num_seconds = int1 * 60
num_seconds_per_cycle = 60
total_loops = int(round(num_seconds / num_seconds_per_cycle, 0)) * 2
num_loops_completed = 0

lower_range = num_seconds_per_cycle - 30
upper_range = num_seconds_per_cycle + 30

for i in range(total_loops):

    pyautogui.moveTo(918, 428, duration = 0)
    print(f'Loading file. {num_seconds_per_cycle} sec per cycle. Progress {num_loops_completed} / {total_loops}')

    current_random_num = random.randint(lower_range, upper_range)
    #print(f'Random # of seconds to sleep: {current_random_num}')

    time.sleep(current_random_num)
    num_loops_completed += 1

