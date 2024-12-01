from common import *

DAY_NUMBER = 1

with get_data(DAY_NUMBER) as f:
    splitted = [line.split() for line in f.readlines()]

    firstList = [int(x[0]) for x in splitted]
    secondList = [int(x[1]) for x in splitted]

firstList.sort()
secondList.sort()

print_result(DAY_NUMBER, 1, sum([abs(x - y) for x, y in zip(firstList, secondList)]))
print_result(DAY_NUMBER, 2, sum([secondList.count(x) * x for x in firstList]))
