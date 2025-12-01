from math import floor
from common import *

DAY_NUMBER = 1

with get_data(DAY_NUMBER) as f:
    instructions = [int(i) for i in [lines.strip().replace('R', '').replace('L', '-') for lines in f.readlines()]]

# Part 1
dial = 50
result = 0

for i in instructions:
    dial += i
    dial %= 100

    if dial == 0:
        result += 1

print_result(DAY_NUMBER, 1, result)

# Part 2
dial = 50
result = 0

for i in instructions:
    was_zero = dial == 0

    dial += i
    result += floor(abs(dial) / 100)
    result += 1 if ((dial < 0 or dial == 0) and not was_zero) else 0

    dial %= 100 

print_result(DAY_NUMBER, 2, result)

