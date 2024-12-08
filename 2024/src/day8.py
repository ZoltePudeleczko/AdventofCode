from common import *

DAY_NUMBER = 8
USE_EXAMPLE = False


with get_data(DAY_NUMBER, USE_EXAMPLE) as f:
    city = [l.strip() for l in f.readlines()]


def is_out_of_board(pos):
    return pos[1] < 0 or pos[0] < 0 or pos[1] >= len(city) or pos[0] >= len(city[0])


def find_other_antennas(antenna, x, y):
    return [
        (i, j)
        for i in range(len(city))
        for j in range(len(city[0]))
        if city[j][i] == antenna and (i, j) != (x, y)
    ]


def get_antinodes(x1, y1, x2, y2, one_antinode_per_line):
    x_diff = x1 - x2
    y_diff = y1 - y2
    antinodes = [(x1, y1), (x2, y2)] if not one_antinode_per_line else []

    def add_antinodes(x, y, x_step, y_step):
        while True:
            x += x_step
            y += y_step

            if is_out_of_board((x, y)):
                break
            antinodes.append((x, y))

            if one_antinode_per_line:
                break

    add_antinodes(x1, y1, x_diff, y_diff)
    add_antinodes(x2, y2, -x_diff, -y_diff)

    return antinodes


def count_antinodes(one_antinode_per_line):
    antinodes = set()
    for x, y in [
        (x, y)
        for x in range(len(city))
        for y in range(len(city[0]))
        if city[y][x] != "."
    ]:
        for x2, y2 in find_other_antennas(city[y][x], x, y):
            for anti in get_antinodes(x, y, x2, y2, one_antinode_per_line):
                if not is_out_of_board(anti):
                    antinodes.add(anti)

    return len(antinodes)


print_result(DAY_NUMBER, 1, count_antinodes(True))
print_result(DAY_NUMBER, 2, count_antinodes(False))
