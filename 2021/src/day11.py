with open('./inputs/day11.txt') as f:
    octopuses = [[int(n) for n in line.strip()] for line in f.readlines()]

octopusesNumber = len(octopuses) * len(octopuses[0])

flashesAfter100 = 0
simultanousStep = -1
for i in range(1000):
    for x in range(len(octopuses)):
        for y in range(len(octopuses[0])):
            octopuses[x][y] += 1

    flashOccured = True
    flashes = 0
    while flashOccured:
        flashOccured = False
        for x in range(len(octopuses)):
            for y in range(len(octopuses[0])):
                if octopuses[x][y] > 9:
                    octopuses[x][y] = -1
                    flashOccured = True
                    flashes += 1

                    if x > 0 and octopuses[x - 1][y] != -1:
                        octopuses[x - 1][y] += 1
                    if x < len(octopuses) - 1 and octopuses[x + 1][y] != -1:
                        octopuses[x + 1][y] += 1
                    if y > 0 and octopuses[x][y - 1] != -1:
                        octopuses[x][y - 1] += 1
                    if y < len(octopuses[0]) - 1 and octopuses[x][y + 1] != -1:
                        octopuses[x][y + 1] += 1
                    if x > 0 and y > 0 and octopuses[x - 1][y - 1] != -1:
                        octopuses[x - 1][y - 1] += 1
                    if x > 0 and y < len(octopuses[0]) - 1 and octopuses[x - 1][y + 1] != -1:
                        octopuses[x - 1][y + 1] += 1
                    if x < len(octopuses) - 1 and y > 0 and octopuses[x + 1][y - 1] != -1:
                        octopuses[x + 1][y - 1] += 1
                    if x < len(octopuses) - 1 and y < len(octopuses[0]) - 1 and octopuses[x + 1][y + 1] != -1:
                        octopuses[x + 1][y + 1] += 1

    if i < 100:
        flashesAfter100 += flashes

    if flashes == octopusesNumber:
        simultanousStep = i + 1

    for x in range(len(octopuses)):
        for y in range(len(octopuses[0])):
            if octopuses[x][y] == -1:
                octopuses[x][y] = 0

    if i >= 100 and simultanousStep != -1:
        break

print(f"11-1: {flashesAfter100}")
print(f"11-2: {simultanousStep}")
