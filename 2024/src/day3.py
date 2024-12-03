import re
from common import *

DAY_NUMBER = 3
USE_EXAMPLE = False

DO_REGEX = "do\(\)"
DO_NOT_REGEX = "don't\(\)"
MUL_REGEX = "mul\([0-9]{1,3},[0-9]{1,3}\)"

with get_data(DAY_NUMBER, USE_EXAMPLE) as f:
    memory = "".join(f.readlines())


def part_one():
    result = 0
    for mul_expression in re.finditer(MUL_REGEX, memory):
        digits = mul_expression.group()[4 : len(mul_expression.group()) - 1].split(",")
        result += int(digits[0]) * int(digits[1])

    return result


def part_two():
    do_instructions = (
        [(-1, True)]
        + [(x.start(), True) for x in re.finditer(DO_REGEX, memory)]
        + [(x.start(), False) for x in re.finditer(DO_NOT_REGEX, memory)]
    )

    result = 0
    for mul_expression in re.finditer(MUL_REGEX, memory):
        do_mul = min(
            enumerate([i for i in do_instructions if i[0] < mul_expression.start()]),
            key=lambda x: abs(mul_expression.start() - x[1][0]),
        )[1][1]

        if not do_mul:
            continue

        digits = mul_expression.group()[4 : len(mul_expression.group()) - 1].split(",")
        result += int(digits[0]) * int(digits[1])

    return result


print_result(DAY_NUMBER, 1, part_one())
print_result(DAY_NUMBER, 2, part_two())
