from collections import namedtuple

with open("../inputs/day5.txt") as f:
    VentLine = namedtuple("VentLine", "x1 y1 x2 y2")
    ventLines = [
        VentLine(int(n[0]), int(n[1]), int(n[2]), int(n[3]))
        for n in [
            line.strip().replace(" -> ", ",").split(",") for line in f.readlines()
        ]
    ]


def count_double_points(ventLines, countHorizontals):
    points = {}

    for line in ventLines:
        if countHorizontals == False and line.x1 != line.x2 and line.y1 != line.y2:
            continue

        if line.x1 == line.x2:
            xmove = 0
        elif line.x1 - line.x2 > 0:
            xmove = -1
        else:
            xmove = 1

        if line.y1 == line.y2:
            ymove = 0
        elif line.y1 - line.y2 > 0:
            ymove = -1
        else:
            ymove = 1

        point = (line.x1, line.y1)
        while point != (line.x2, line.y2):
            if point in points:
                points[point] = points[point] + 1
            else:
                points[point] = 1
            point = (point[0] + xmove, point[1] + ymove)
        if point in points:
            points[point] = points[point] + 1
        else:
            points[point] = 1

    return len([1 for i in list(points.values()) if i >= 2])


print(f"5-1: {count_double_points(ventLines, False)}")
print(f"5-2: {count_double_points(ventLines, True)}")
