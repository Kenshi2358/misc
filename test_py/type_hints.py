from typing import List


def addition(list1: List[int]) -> int:

    sum = 0
    for each_item in list1:
        sum += each_item

    return sum


result = addition([1, 2, 3])

print(result)
pass
