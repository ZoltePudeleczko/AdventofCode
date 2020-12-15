with open('../inputs/day15.txt') as f:
    numbers = [int(n) for n in f.readlines()[0].split(',')]

indexes = {}
for i in range(len(numbers) - 1):
    indexes[numbers[i]] = i + 1
lastNumber = numbers[-1]
turn = len(numbers)
while turn < 30000000:
    turn += 1
    if lastNumber not in indexes.keys():
        indexes[lastNumber] = turn - 1
        lastNumber = 0
    else:
        tempNumber = turn - 1 - indexes[lastNumber]
        indexes[lastNumber] = turn - 1
        lastNumber = tempNumber
    
    if turn == 2020:
        print(f"15-1: {lastNumber}")

print(f"15-2: {lastNumber}")
