from math import floor
from common import *

DAY_NUMBER = 2

with get_data(DAY_NUMBER) as f:
    ranges = [range.split('-') for range in [line.strip().split(',') for line in f.readlines()][0]]

# Part 1
result = 0

for r in ranges:
    for number in range(int(r[0]), int(r[1]) + 1):
        num_str = str(number)   

        if num_str[:len(num_str)//2] == num_str[len(num_str)//2:]:
            result += number

print_result(DAY_NUMBER, 1, result)

# Part 2
result = 0

for r in ranges:
    for number in range(int(r[0]), int(r[1]) + 1):
        num_str = str(number)

        found = False
        for substr_len in range(1, len(num_str) // 2 + 1):
            if len(num_str) % substr_len == 0:
                substr = num_str[:substr_len]
                num_repeats = len(num_str) // substr_len
                if num_repeats >= 2 and substr * num_repeats == num_str:
                    found = True
                    break
        if found:
            result += number

print_result(DAY_NUMBER, 2, result)

