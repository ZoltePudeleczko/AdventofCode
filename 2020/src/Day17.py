def count_active_neighbours(cubes, cur_cube):
    active = 0
    for x in [cur_cube[0] - 1, cur_cube[0], cur_cube[0] + 1]:
        for y in [cur_cube[1] - 1, cur_cube[1], cur_cube[1] + 1]:
            for z in [cur_cube[2] - 1, cur_cube[2], cur_cube[2] + 1]:
                if (x, y, z) == cur_cube:
                    continue
                if (x, y, z) in cubes.keys() and cubes[(x, y, z)] == '#':
                    active += 1
    return active


def count_active_neighbours4d(cubes, cur_cube):
    active = 0
    for x in [cur_cube[0] - 1, cur_cube[0], cur_cube[0] + 1]:
        for y in [cur_cube[1] - 1, cur_cube[1], cur_cube[1] + 1]:
            for z in [cur_cube[2] - 1, cur_cube[2], cur_cube[2] + 1]:
                for w in [cur_cube[3] - 1, cur_cube[3], cur_cube[3] + 1]:
                    if (x, y, z, w) == cur_cube:
                        continue
                    if (x, y, z, w) in cubes.keys() and cubes[(x, y, z, w)] == '#':
                        active += 1
    return active


def grow_cube(xValues, yValues, zValues, cubes):
    for x in range(xValues[0], xValues[1]):
        for y in range(yValues[0], yValues[1]):
            for z in range(zValues[0], zValues[1] + 1):
                if (x, y, z) not in cubes.keys():
                    cubes[(x, y, z)] = '.'
    return cubes


def grow_cube4d(xValues, yValues, zValues, wValues, cubes):
    for x in range(xValues[0], xValues[1]):
        for y in range(yValues[0], yValues[1]):
            for z in range(zValues[0], zValues[1] + 1):
                for w in range(wValues[0], wValues[1] + 1):
                    if (x, y, z, w) not in cubes.keys():
                        cubes[(x, y, z, w)] = '.'
    return cubes

with open('../inputs/day17.txt') as f:
    lines = [list(line.strip()) for line in f.readlines()]

cubes = {}
for y in range(len(lines)):
    for x in range(len(lines[y])):
        cubes[(x, y, 0)] = lines[y][x]

xValues = [0, len(lines[0])]
yValues = [0, len(lines)]
zValues = [0, 0]
for i in range(6):
    xValues = [xValues[0] - 1, xValues[1] + 1]
    yValues = [yValues[0] - 1, yValues[1] + 1]
    zValues = [zValues[0] - 1, zValues[1] + 1]
    cubes = grow_cube(xValues, yValues, zValues, cubes)
    toChange = []
    for cube in cubes.keys():
        active = count_active_neighbours(cubes, cube)
        if cubes[cube] == '#' and active not in [2, 3]:
            toChange.append(cube)
        elif cubes[cube] == '.' and active == 3:
            toChange.append(cube)
    for cube in toChange:
        if cubes[cube] == '#':
            cubes[cube] = '.'
        else:
            cubes[cube] = '#'

print(f"17-1: {sum([1 for value in cubes.values() if value == '#'])}")

cubes4d = {}
for y in range(len(lines)):
    for x in range(len(lines[y])):
        cubes4d[(x, y, 0, 0)] = lines[y][x]

xValues = [0, len(lines[0])]
yValues = [0, len(lines)]
zValues = [0, 0]
wValues = [0, 0]
for i in range(6):
    xValues = [xValues[0] - 1, xValues[1] + 1]
    yValues = [yValues[0] - 1, yValues[1] + 1]
    zValues = [zValues[0] - 1, zValues[1] + 1]
    wValues = [wValues[0] - 1, wValues[1] + 1]
    cubes4d = grow_cube4d(xValues, yValues, zValues, wValues, cubes4d)
    toChange = []
    for cube in cubes4d.keys():
        active = count_active_neighbours4d(cubes4d, cube)
        if cubes4d[cube] == '#' and active not in [2, 3]:
            toChange.append(cube)
        elif cubes4d[cube] == '.' and active == 3:
            toChange.append(cube)
    for cube in toChange:
        if cubes4d[cube] == '#':
            cubes4d[cube] = '.'
        else:
            cubes4d[cube] = '#'

print(f"17-2: {sum([1 for value in cubes4d.values() if value == '#'])}")
