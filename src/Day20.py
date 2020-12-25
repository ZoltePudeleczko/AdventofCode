import numpy as np


class ImageTile:
    def __init__(self, tile, number):
        self.tile = tile
        self.number = number

    def top(self):
        return self.tile[0]

    def down(self):
        return self.tile[-1]

    def right(self):
        return ''.join(t[-1] for t in self.tile)

    def left(self):
        return ''.join(t[0] for t in self.tile)


def check(image_tile, image, edge_size):
    if len(image) + 1 - edge_size > 0:
        if image_tile.top() != image[len(image) - edge_size].down():
            return False
    if (len(image) + 1) % edge_size != 1:
        if image_tile.left() != image[len(image) - 1].right():
            return False
    return True


def build_image(image_tiles, edge_size, image=[], done=[]):
    if len(image) == len(image_tiles):
        return image

    for tile_options in image_tiles:
        if tile_options not in done:
            for t in tile_options:
                if check(t, image, edge_size):
                    result = build_image(image_tiles, edge_size, image + [t], done + [tile_options])
                    if result:
                        return result


with open('../inputs/day20.txt') as f:
    lines = f.readlines()
    imageTiles = []
    newTile = 1
    for line in lines:
        if line == '\n':
            tileOptions = [
                ImageTile(tile, tileNr),
                ImageTile(np.rot90(tile, 1).tolist(), tileNr),
                ImageTile(np.rot90(tile, 2).tolist(), tileNr),
                ImageTile(np.rot90(tile, 3).tolist(), tileNr),
                ImageTile(np.flipud(tile).tolist(), tileNr),
                ImageTile(np.rot90(np.flipud(tile), 1).tolist(), tileNr),
                ImageTile(np.rot90(np.flipud(tile), 2).tolist(), tileNr),
                ImageTile(np.rot90(np.flipud(tile), 3).tolist(), tileNr),
            ]
            imageTiles.append(tileOptions)
            newTile = 1
        elif newTile:
            tileNr = int(line[line.index(' ') + 1:-2])
            tile = []
            newTile = 0
        else:
            tile.append(list(line.strip()))
    tileOptions = [
        ImageTile(tile, tileNr),
        ImageTile(np.rot90(tile, 1).tolist(), tileNr),
        ImageTile(np.rot90(tile, 2).tolist(), tileNr),
        ImageTile(np.rot90(tile, 3).tolist(), tileNr),
        ImageTile(np.flipud(tile).tolist(), tileNr),
        ImageTile(np.rot90(np.flipud(tile), 1).tolist(), tileNr),
        ImageTile(np.rot90(np.flipud(tile), 2).tolist(), tileNr),
        ImageTile(np.rot90(np.flipud(tile), 3).tolist(), tileNr),
    ]
    imageTiles.append(tileOptions)


edge_size = int(len(imageTiles) ** 0.5)
image = build_image(imageTiles, edge_size)

print(f"20-1: {image[0].number * image[11].number * image[-1].number * image[-12].number}")
