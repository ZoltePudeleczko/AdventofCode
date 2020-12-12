directions = {
    'north': 0,
    'east': 1,
    'south': 2,
    'west': 3
}

with open('../inputs/day12.txt') as f:
    actions = [(line[0], int(line[1:])) for line in f.readlines()]

facing = directions['east']
x = y = 0
for action in actions:
    if action[0] is 'N':
        y += action[1]
    elif action[0] is 'S':
        y -= action[1]
    elif action[0] is 'E':
        x += action[1]
    elif action[0] is 'W':
        x -= action[1]
    elif action[0] is 'L':
        facing = int((facing - (action[1] / 90)) % 4)
    elif action[0] is 'R':
        facing = int((facing + (action[1] / 90)) % 4)
    elif action[0] is 'F':
        if facing is directions['north']:
            y += action[1]
        if facing is directions['east']:
            x += action[1]
        if facing is directions['south']:
            y -= action[1]
        if facing is directions['west']:
            x -= action[1]

print(f"12-1: {abs(x) + abs(y)}")

waypointX = 10
waypointY = 1
waypointXDirection = directions['east']
waypointYDirection = directions['north']
x = y = 0
for action in actions:
    if action[0] is 'N':
        waypointY += action[1]
        if waypointY > 0:
            waypointYDirection = directions['north']
    elif action[0] is 'S':
        waypointY -= action[1]
        if waypointY < 0:
            waypointYDirection = directions['south']
    elif action[0] is 'E':
        waypointX += action[1]
        if waypointX > 0:
            waypointXDirection = directions['east']
    elif action[0] is 'W':
        waypointX -= action[1]
        if waypointX < 0:
            waypointXDirection = directions['west']
    elif action[0] in ['L', 'R']:
        if action[0] == 'L':
            waypointXDirection = int((waypointXDirection - (action[1] / 90)) % 4)
            waypointYDirection = int((waypointYDirection - (action[1] / 90)) % 4)
        elif action[0] == 'R':
            waypointXDirection = int((waypointXDirection + (action[1] / 90)) % 4)
            waypointYDirection = int((waypointYDirection + (action[1] / 90)) % 4)
        if waypointYDirection in [directions['east'], directions['west']]:
            waypointYDirection, waypointXDirection = waypointXDirection, waypointYDirection
            waypointY, waypointX = waypointX, waypointY

        if waypointYDirection is directions['north'] and waypointY < 0:
            waypointY = -waypointY
        if waypointXDirection is directions['east'] and waypointX < 0:
            waypointX = -waypointX
        if waypointYDirection is directions['south'] and waypointY > 0:
            waypointY = -waypointY
        if waypointXDirection is directions['west'] and waypointX > 0:
            waypointX = -waypointX
    elif action[0] is 'F':
        x += action[1] * waypointX
        y += action[1] * waypointY

print(f"12-2: {abs(x) + abs(y)}")
