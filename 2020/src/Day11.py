with open('../inputs/day11.txt') as f:
    grid = [list(f.replace('\n', '')) for f in f.readlines()]

gridBackup = [row[:] for row in grid]

occupied = 0
changed = 1
while changed:
    changed = 0
    neighboursOccupied = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                Neighbours = []
                if i - 1 >= 0:
                    Neighbours.append(grid[i-1][j])
                    if j - 1 >= 0:
                        Neighbours.append(grid[i-1][j-1])
                    if j + 1 < len(grid[0]):
                        Neighbours.append(grid[i-1][j+1])
                if j - 1 >= 0:
                    Neighbours.append(grid[i][j-1])
                if j + 1 < len(grid[0]):
                    Neighbours.append(grid[i][j+1])
                if i + 1 < len(grid):
                    Neighbours.append(grid[i+1][j])
                    if j - 1 >= 0:
                        Neighbours.append(grid[i+1][j-1])
                    if j + 1 < len(grid[0]):
                        Neighbours.append(grid[i+1][j+1])
                
                neighboursOccupied[(i, j)] = Neighbours.count('#')

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L' and neighboursOccupied[(i, j)] == 0:
                grid[i][j] = '#'
                occupied += 1
                changed = 1
            elif grid[i][j] == '#' and neighboursOccupied[(i, j)] >= 4:
                grid[i][j] = 'L'
                occupied -= 1
                changed = 1

print(f"11-1: {occupied}")

grid = gridBackup.copy()
occupied = 0
changed = 1
while changed:
    changed = 0
    neighboursOccupied = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                Neighbours = []
                for x in range(i - 1, -1, -1):
                    if grid[x][j] != '.':
                        Neighbours.append(grid[x][j])
                        break
                for x in range(i + 1, len(grid)):
                    if grid[x][j] != '.':
                        Neighbours.append(grid[x][j])
                        break
                for y in range(j - 1, -1, -1):
                    if grid[i][y] != '.':
                        Neighbours.append(grid[i][y])
                        break
                for y in range(j + 1, len(grid[0])):
                    if grid[i][y] != '.':
                        Neighbours.append(grid[i][y])
                        break

                iterator = 1
                while i - iterator >= 0 and j - iterator >= 0:
                    if grid[i - iterator][j - iterator] != '.':
                        Neighbours.append(grid[i - iterator][j - iterator])
                        break
                    iterator += 1
                iterator = 1
                while i - iterator >= 0 and j + iterator < len(grid[0]):
                    if grid[i - iterator][j + iterator] != '.':
                        Neighbours.append(grid[i - iterator][j + iterator])
                        break
                    iterator += 1 
                iterator = 1
                while i + iterator < len(grid) and j - iterator >= 0:
                    if grid[i + iterator][j - iterator] != '.':
                        Neighbours.append(grid[i + iterator][j - iterator])
                        break
                    iterator += 1
                iterator = 1
                while i + iterator < len(grid) and j + iterator < len(grid[0]):
                    if grid[i + iterator][j + iterator] != '.':
                        Neighbours.append(grid[i + iterator][j + iterator])
                        break
                    iterator += 1
                
                neighboursOccupied[(i, j)] = Neighbours.count('#')

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L' and neighboursOccupied[(i, j)] == 0:
                grid[i][j] = '#'
                occupied += 1
                changed = 1
            elif grid[i][j] == '#' and neighboursOccupied[(i, j)] >= 5:
                grid[i][j] = 'L'
                occupied -= 1
                changed = 1

print(f"11-2: {occupied}")