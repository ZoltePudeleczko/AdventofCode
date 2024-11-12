with open("../inputs/day7.txt") as f:
    crabs = [int(n) for n in f.readline().strip().split(",")]


def check_fuel_spent(positions, checkValue):
    cost = 0
    for p in positions:
        cost += abs(p - checkValue)
    return cost


def check_fuel_spent_fixed(positions, checkValue):
    cost = 0
    for p in positions:
        move = abs(p - checkValue)
        if move > 0:
            cost += (1 + move) * (move / 2)
    return int(cost)


bestHorizontal = None
bestHorizontal2 = None
for i in range(min(crabs), max(crabs)):
    cost = check_fuel_spent(crabs, i)
    if bestHorizontal == None or cost < bestHorizontal:
        bestHorizontal = cost

    cost = check_fuel_spent_fixed(crabs, i)
    if bestHorizontal2 == None or cost < bestHorizontal2:
        bestHorizontal2 = cost

print(f"7-1: {bestHorizontal}")
print(f"7-2: {bestHorizontal2}")
