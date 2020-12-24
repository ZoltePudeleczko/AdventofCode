def crab_game(cupCircle, current, rounds):
    minValue = min(cupCircle.keys())
    maxValue = max(cupCircle.keys())
    for i in range(rounds):
        removedCups = [
            cupCircle[current],
            cupCircle[cupCircle[current]],
            cupCircle[cupCircle[cupCircle[current]]]
        ]
        cupCircle[current] = cupCircle[cupCircle[cupCircle[cupCircle[current]]]]
        destination = -1
        searchingFor = current
        while destination == -1:
            searchingFor -= 1
            if searchingFor < minValue:
                searchingFor = maxValue

            if searchingFor not in removedCups:
                destination = searchingFor

        tempCup = cupCircle[destination]
        cupCircle[destination] = removedCups[0]
        cupCircle[removedCups[0]] = removedCups[1]
        cupCircle[removedCups[1]] = removedCups[2]
        cupCircle[removedCups[2]] = tempCup

        current = cupCircle[current]
    return cupCircle


with open('../inputs/day23.txt') as f:
    cupCircleBase = [int(c) for c in f.readline().strip()]

cupCircle = {}
for i in range(len(cupCircleBase)):
    cupCircle[cupCircleBase[i]] = cupCircleBase[(i + 1) % len(cupCircleBase)]

cupCircle = crab_game(cupCircle, cupCircleBase[0], 100)

labels = ''
value = 1
while cupCircle[value] != 1:
    value = cupCircle[value]
    labels += f"{value}"

print(f"23-1: {labels}")

cupCircle = {}
for i in range(len(cupCircleBase) - 1):
    cupCircle[cupCircleBase[i]] = cupCircleBase[(i + 1) % len(cupCircleBase)]
cupCircle[cupCircleBase[-1]] = max(cupCircleBase) + 1
for i in range(len(cupCircleBase) + 1, 1000000):
    cupCircle[i] = i + 1
cupCircle[1000000] = cupCircleBase[0]

cupCircle = crab_game(cupCircle, cupCircleBase[0], 10000000)

print(f"23-2: {cupCircle[1] * cupCircle[cupCircle[1]]}")
