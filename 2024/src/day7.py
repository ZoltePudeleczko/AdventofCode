import re
from common import *

DAY_NUMBER = 7
USE_EXAMPLE = False


with get_data(DAY_NUMBER, USE_EXAMPLE) as f:
    lines = [re.split(": | ", l.strip()) for l in f.readlines()]


def recursive_equation(arguments, expected, result, current_index, operators):
    if current_index == len(arguments):
        if result == expected:
            return True
        return False

    for operator in operators:
        if operator == "+":
            new_result = result + arguments[current_index]
        elif operator == "*":
            new_result = result * arguments[current_index]
        elif operator == "||":
            new_result = int(str(result) + str(arguments[current_index]))

        if new_result > expected:
            continue

        if recursive_equation(
            arguments, expected, new_result, current_index + 1, operators
        ):
            return True

    return False


def is_possible_equation(line, operators):
    expected = int(line[0])
    arguments = [int(x) for x in line[1:]]

    return recursive_equation(arguments, expected, arguments[0], 1, operators)


def part_one():
    return sum(int(line[0]) for line in lines if is_possible_equation(line, ["+", "*"]))


def part_two():
    return sum(
        int(line[0]) for line in lines if is_possible_equation(line, ["+", "*", "||"])
    )


print_result(DAY_NUMBER, 1, part_one())
print_result(DAY_NUMBER, 2, part_two())
