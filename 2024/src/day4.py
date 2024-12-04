from common import *

DAY_NUMBER = 4
USE_EXAMPLE = False

ALL_DIRECTIONS = [
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
    (0, -1),
    (-1, 0),
]
XMAS_SHAPES = [
    "MMASS",
    "MSAMS",
    "SMASM",
    "SSAMM",
]
WORD = "XMAS"

with get_data(DAY_NUMBER, USE_EXAMPLE) as f:
    board = [l.strip() for l in f.readlines()]


def get_value_if_exists(x, y):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
        return None

    return board[y][x]


def part_one():
    count = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[y][x] != WORD[0]:
                continue

            for direction in ALL_DIRECTIONS:
                created_word = WORD[0]
                for i in range(1, len(WORD)):
                    next_value = get_value_if_exists(
                        x + i * direction[0], y + i * direction[1]
                    )
                    if next_value != WORD[i]:
                        break

                    created_word += next_value

                if created_word == WORD:
                    count += 1

    return count


def get_x_shape(x, y):
    return (
        board[y][x]
        + board[y][x + 2]
        + board[y + 1][x + 1]
        + board[y + 2][x]
        + board[y + 2][x + 2]
    )


def is_a_xmas_shape(shape):
    return any(shape == xmas_shape for xmas_shape in XMAS_SHAPES)


def part_two():
    count = 0
    for y in range(len(board[0]) - 2):
        for x in range(len(board) - 2):
            if is_a_xmas_shape(get_x_shape(x, y)):
                count += 1
    return count


print_result(DAY_NUMBER, 1, part_one())
print_result(DAY_NUMBER, 2, part_two())
