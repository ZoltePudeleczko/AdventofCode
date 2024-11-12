import copy
from dataclasses import dataclass


@dataclass
class CaveDetails:
    name: str
    isBig: bool
    connections: set
    visited: int = 0


with open("../inputs/day12.txt") as f:
    connections = [line.strip().split("-") for line in f.readlines()]

caves = {}
for connection in connections:
    if connection[0] not in caves:
        caves[connection[0]] = CaveDetails(
            connection[0], connection[0].isupper(), set()
        )
    if connection[1] not in caves:
        caves[connection[1]] = CaveDetails(
            connection[1], connection[1].isupper(), set()
        )

    caves[connection[0]].connections.add(connection[1])
    caves[connection[1]].connections.add(connection[0])


def explore_the_caves(caveName, cavesStatus):
    cavesStatus[caveName].visited += 1

    if caveName == "end":
        return 1

    localRoutes = 0
    for connection in cavesStatus[caveName].connections:
        if cavesStatus[connection].isBig or cavesStatus[connection].visited == 0:
            localRoutes += explore_the_caves(connection, copy.deepcopy(cavesStatus))

    return localRoutes


def explore_the_caves_special(caveName, cavesStatus, specialCaveName):
    cavesStatus[caveName].visited += 1

    if caveName == "end":
        if cavesStatus[specialCaveName].visited == 2:
            return 1
        else:
            return 0

    localRoutes = 0
    for connection in cavesStatus[caveName].connections:
        if (
            cavesStatus[connection].isBig
            or (connection == specialCaveName and cavesStatus[connection].visited < 2)
            or cavesStatus[connection].visited == 0
        ):
            localRoutes += explore_the_caves_special(
                connection, copy.deepcopy(cavesStatus), specialCaveName
            )

    return localRoutes


normalPaths = explore_the_caves("start", copy.deepcopy(caves))
specialPaths = normalPaths

for cave in caves.values():
    if not cave.isBig and cave.name not in ("start", "end"):
        specialPaths += explore_the_caves_special(
            "start", copy.deepcopy(caves), cave.name
        )

print(f"12-1: {normalPaths}")
print(f"12-2: {specialPaths}")
