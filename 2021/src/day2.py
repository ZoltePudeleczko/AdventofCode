with open('./inputs/day2.txt') as f:
    commands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in f.readlines()]

position = [0, 0]
for c in commands:
    if c[0] == 'forward':
        position[0] += c[1]
    elif c[0] == 'up':
        position[1] -= c[1]
    elif c[0] == 'down':
        position[1] += c[1]

print(f"2-1: {position} {position[0] * position[1]}")

aim = 0
position = [0, 0]
for c in commands:
    if c[0] == 'forward':
        position[0] += c[1]
        position[1] += aim * c[1]
    elif c[0] == 'up':
        aim -= c[1]
    elif c[0] == 'down':
        aim += c[1]

print(f"2-2: {position} {position[0] * position[1]}")
