from common import *

DAY_NUMBER = 10
USE_EXAMPLE = False


with get_data(DAY_NUMBER, USE_EXAMPLE) as f:
    topography = [l.strip() for l in f.readlines()]


def is_out_of_map(pos):
    return (
        pos[1] < 0
        or pos[0] < 0
        or pos[1] >= len(topography)
        or pos[0] >= len(topography[0])
    )


def get_rating(head, end):
    def dfs(pos, visited):
        if pos == end:
            return 1
        visited.add(pos)
        count = 0
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if (
                not is_out_of_map(new_pos)
                and new_pos not in visited
                and int(topography[new_pos[1]][new_pos[0]])
                == int(topography[pos[1]][pos[0]]) + 1
            ):
                count += dfs(new_pos, visited.copy())
        return count

    return dfs(head, set())


trailheads_ratings = [
    get_rating(head, end)
    for head in [
        (x, y)
        for x in range(len(topography[0]))
        for y in range(len(topography))
        if topography[y][x] == "0"
    ]
    for end in [
        (x, y)
        for x in range(len(topography[0]))
        for y in range(len(topography))
        if topography[y][x] == "9"
    ]
]

print_result(DAY_NUMBER, 1, sum(1 for rating in trailheads_ratings if rating > 0))
print_result(DAY_NUMBER, 2, sum(trailheads_ratings))
