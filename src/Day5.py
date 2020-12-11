with open('inputs/day5.txt') as f:
    boardingPasses = f.readlines()

seatIds = []
for bp in boardingPasses:
    rowLow = 0
    rowHigh = 127
    for c in bp[:6]:
        if c is 'F':
            rowHigh -= int((rowHigh - rowLow) / 2) + 1
        if c is 'B':
            rowLow += int((rowHigh - rowLow) / 2) + 1
    columnLow = 0
    columnHigh = 7
    for c in bp[7:9]:
        if c is 'L':
            columnHigh -= int((columnHigh - columnLow) / 2) + 1
        if c is 'R':
            columnLow += int((columnHigh - columnLow) / 2) + 1
    row = rowLow if bp[6] is 'F' else rowHigh
    column = columnLow if bp[9] is 'L' else columnHigh
    seatId = row * 8 + column
    seatIds.append(seatId)

print(f"5-1: {max(seatIds)}")

missing = [seatId for seatId in range(min(seatIds), max(seatIds)) if seatId not in seatIds]
print(f"5-2: {missing}")
