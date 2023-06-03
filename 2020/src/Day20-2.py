import os.path
import numpy as np


def search_monsters(image, sea_monster):
    for i in range(len(image) - len(sea_monster)):
        for j in range(len(image[i]) - len(sea_monster[0])):
            monsterFound = True
            monsterElements = []
            for y in range(len(sea_monster)):
                for x in range(len(sea_monster[y])):
                    if sea_monster[y][x] == ' ':
                        continue
                    elif sea_monster[y][x] == '#':
                        if image[i + y][j + x] != '#':
                            monsterFound = False
                            break
                        else:
                            monsterElements.append((i + y, j + x))
                if not monsterFound:
                    break
            if monsterFound:
                for element in monsterElements:
                    image[element[0]][element[1]] = '@'
    return image


def count_rough_water(image):
    rough_waters = 0
    for line in image:
        for c in line:
            if c == '#':
                rough_waters += 1
    return rough_waters


if not os.path.exists('../inputs/day20-2.txt'):
    exec(open("./Day20.py").read())

with open('../inputs/day20-2.txt') as f:
    image = []
    for line in f.readlines():
        image.append(list(line.strip()))

sea_monster = """                  #
#    ##    ##    ###
 #  #  #  #  #  #   """
sea_monster = sea_monster.split('\n')

imageOptions = [
    image,
    np.rot90(image, 1).tolist(),
    np.rot90(image, 2).tolist(),
    np.rot90(image, 3).tolist(),
    np.flipud(image).tolist(),
    np.rot90(np.flipud(image), 1).tolist(),
    np.rot90(np.flipud(image), 2).tolist(),
    np.rot90(np.flipud(image), 3).tolist(),
]

rough_waters = []
for im in imageOptions:
    rough_waters.append(count_rough_water(search_monsters(im, sea_monster)))

print(f"20-2: {min(rough_waters)}")
