with open("../inputs/day9.txt") as f:
    heightmap = [line.strip() for line in f.readlines()]

riskLevel = 0
for y in range(len(heightmap)):
    for x in range(len(heightmap[y])):
        if x - 1 < 0 or int(heightmap[y][x - 1]) > int(heightmap[y][x]):
            if x + 1 >= len(heightmap[y]) or int(heightmap[y][x + 1]) > int(
                heightmap[y][x]
            ):
                if y - 1 < 0 or int(heightmap[y - 1][x]) > int(heightmap[y][x]):
                    if y + 1 >= len(heightmap) or int(heightmap[y + 1][x]) > int(
                        heightmap[y][x]
                    ):
                        riskLevel += int(heightmap[y][x]) + 1


def fill_basinmap(y, x, basinNumber):
    if y >= 0 and y < len(basinmap):
        if x >= 0 and x < len(basinmap[0]):
            if heightmap[y][x] != "9":
                if basinmap[y][x] == 0:
                    basinmap[y][x] = basinNumber
                    fill_basinmap(y - 1, x, basinNumber)
                    fill_basinmap(y + 1, x, basinNumber)
                    fill_basinmap(y, x - 1, basinNumber)
                    fill_basinmap(y, x + 1, basinNumber)
            else:
                basinmap[y][x] = -1


def count_occurances(value):
    count = 0
    for y in range(len(basinmap)):
        for x in range(len(basinmap[y])):
            if basinmap[y][x] == value:
                count += 1
    return count


basinmap = [x[:] for x in [[0] * len(heightmap[0])] * len(heightmap)]
basinNumber = 0
for y in range(len(basinmap)):
    for x in range(len(basinmap[y])):
        if basinmap[y][x] == 0:
            if heightmap[y][x] != "9":
                basinNumber += 1
                fill_basinmap(y, x, basinNumber)
            else:
                basinmap[y][x] = -1

basinSizes = [0] * basinNumber
for x in range(basinNumber):
    basinSizes[x] = count_occurances(x + 1)

basinSizes.sort(reverse=1)

print(f"9-1: {riskLevel}")
print(f"9-2: {basinSizes[0] * basinSizes[1] * basinSizes[2]}")
