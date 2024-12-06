from common import *
from enum import Enum

DAY_NUMBER = 6
USE_EXAMPLE = False


class DIRECTION(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


with get_data(DAY_NUMBER, USE_EXAMPLE) as f:
    board = [l.strip() for l in f.readlines()]


def is_out_of_board(pos):
    return pos[1] < 0 or pos[0] < 0 or pos[1] >= len(board) or pos[0] >= len(board[0])


def get_guard_position():
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[y][x] == "^":
                return (y, x)


def get_next_position(pos, direction):
    match direction:
        case DIRECTION.UP:
            return (pos[0] - 1, pos[1])
        case DIRECTION.RIGHT:
            return (pos[0], pos[1] + 1)
        case DIRECTION.DOWN:
            return (pos[0] + 1, pos[1])
        case DIRECTION.LEFT:
            return (pos[0], pos[1] - 1)


def turn_right(direction):
    match direction:
        case DIRECTION.UP:
            return DIRECTION.RIGHT
        case DIRECTION.RIGHT:
            return DIRECTION.DOWN
        case DIRECTION.DOWN:
            return DIRECTION.LEFT
        case DIRECTION.LEFT:
            return DIRECTION.UP


def get_route_length(board, guard, direction):
    visited = set()
    visited_with_direction = set()
    while True:
        if (guard, direction) in visited_with_direction:
            return None

        visited.add(guard)
        visited_with_direction.add((guard, direction))

        next = get_next_position(guard, direction)
        if is_out_of_board(next):
            break

        if board[next[0]][next[1]] == "#":
            direction = turn_right(direction)
            continue

        guard = next

    return len(visited)


def part_one(guard, direction):
    return get_route_length(board, guard, direction)


def part_two(guard, direction):
    count = 0

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[y][x] != ".":
                continue

            new_board = board.copy()
            new_board[y] = new_board[y][:x] + "#" + new_board[y][x + 1 :]

            if get_route_length(new_board, guard, direction) is None:
                count += 1

    return count


guard = get_guard_position()
print_result(DAY_NUMBER, 1, part_one(guard, DIRECTION.UP))
print_result(DAY_NUMBER, 2, part_two(guard, DIRECTION.UP))
