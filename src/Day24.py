with open('../inputs/day24.txt') as f:
    directions = [d.strip() for d in f.readlines()]

blackTiles = []
for direction in directions:
    position = [0, 0]
    last = ''
    for i in range(len(direction)):
        if last == 's':
            last = direction[i]
            if last == 'e':
                position[0] += 1
                position[1] -= 1
            elif last == 'w':
                position[1] -= 1
        elif last == 'n':
            last = direction[i]
            if last == 'e':
                position[1] += 1
            elif last == 'w':
                position[0] -= 1
                position[1] += 1
        else:
            last = direction[i]
            if last == 'e':
                position[0] += 1
            elif last == 'w':
                position[0] -= 1
    if (position[0], position[1]) in blackTiles:
        blackTiles.remove((position[0], position[1]))
    else:
        blackTiles.append((position[0], position[1]))

print(f"24-1: {len(blackTiles)}")

for i in range(100):
    flip = []
    for black in blackTiles:
        blackNeighbours = 0
        if (black[0], black[1] + 1) in blackTiles:
            blackNeighbours += 1
        if (black[0] + 1, black[1]) in blackTiles:
            blackNeighbours += 1
        if (black[0] + 1, black[1] - 1) in blackTiles:
            blackNeighbours += 1
        if (black[0], black[1] - 1) in blackTiles:
            blackNeighbours += 1
        if (black[0] - 1, black[1]) in blackTiles:
            blackNeighbours += 1
        if (black[0] - 1, black[1] + 1) in blackTiles:
            blackNeighbours += 1

        if blackNeighbours == 0 or blackNeighbours > 2:
            flip.append(black)

    whiteTiles = {}
    for black in blackTiles:
        if (black[0], black[1] + 1) not in blackTiles:
            if (black[0], black[1] + 1) not in whiteTiles.keys():
                whiteTiles[(black[0], black[1] + 1)] = 1
            else:
                whiteTiles[(black[0], black[1] + 1)] += 1
        if (black[0] + 1, black[1]) not in blackTiles:
            if (black[0] + 1, black[1]) not in whiteTiles.keys():
                whiteTiles[(black[0] + 1, black[1])] = 1
            else:
                whiteTiles[(black[0] + 1, black[1])] += 1
        if (black[0] + 1, black[1] - 1) not in blackTiles:
            if (black[0] + 1, black[1] - 1) not in whiteTiles.keys():
                whiteTiles[(black[0] + 1, black[1] - 1)] = 1
            else:
                whiteTiles[(black[0] + 1, black[1] - 1)] += 1
        if (black[0], black[1] - 1) not in blackTiles:
            if (black[0], black[1] - 1) not in whiteTiles.keys():
                whiteTiles[(black[0], black[1] - 1)] = 1
            else:
                whiteTiles[(black[0], black[1] - 1)] += 1
        if (black[0] - 1, black[1]) not in blackTiles:
            if (black[0] - 1, black[1]) not in whiteTiles.keys():
                whiteTiles[(black[0] - 1, black[1])] = 1
            else:
                whiteTiles[(black[0] - 1, black[1])] += 1
        if (black[0] - 1, black[1] + 1) not in blackTiles:
            if (black[0] - 1, black[1] + 1) not in whiteTiles.keys():
                whiteTiles[(black[0] - 1, black[1] + 1)] = 1
            else:
                whiteTiles[(black[0] - 1, black[1] + 1)] += 1

    for white in whiteTiles.keys():
        if whiteTiles[white] == 2:
            flip.append(white)

    for f in flip:
        if f in blackTiles:
            blackTiles.remove(f)
        else:
            blackTiles.append(f)

print(f"24-2: {len(blackTiles)}")
