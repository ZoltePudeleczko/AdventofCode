with open("../inputs/day1.txt") as f:
    depths = [int(line) for line in f.readlines()]

increaments = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        increaments += 1

print(f"1-1: {increaments}")

increaments = 0
for i in range(3, len(depths)):
    if depths[i] > depths[i - 3]:
        increaments += 1

print(f"1-2: {increaments}")
