def slope(tobogganMap, right, down):
    position = [0, 0]

    trees = 0
    while(position[0] < len(tobogganMap)):
        if tobogganMap[position[0]][position[1]] == '#':
            trees += 1
        position[0] += down
        position[1] = (position[1] + right) % (len(tobogganMap[0]) - 1)
    
    return trees

with open('inputs/day3.txt') as f:
    tobogganMap = f.readlines()

print(f"3-1: {slope(tobogganMap, 3, 1)}")
print(f"3-2: {slope(tobogganMap, 1, 1) * slope(tobogganMap, 3, 1) * slope(tobogganMap, 5, 1) * slope(tobogganMap, 7, 1) * slope(tobogganMap, 1, 2)}")