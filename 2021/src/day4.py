with open("../inputs/day4.txt") as f:
    lines = [line.strip() for line in f.readlines()]

drawnNumbers = [int(number) for number in lines[0].split(",")]

boards = []
newBoard = []
for line in lines[2:]:
    if line == "":
        boards.append(newBoard)
        newBoard = []
    else:
        newBoard.append([int(number) for number in line.split()])
boards.append(newBoard)


def mark_number(boards, number):
    for board in boards:
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == number:
                    board[y][x] = -1


def check_for_bingo(board):
    bingo = False
    for y in range(len(board)):
        bingoChance = True
        for x in range(len(board[y])):
            if board[y][x] != -1:
                bingoChance = False
                break
        if bingoChance == True:
            bingo = True
            break

    if bingo == False:
        for x in range(len(board[0])):
            bingoChance = True
            for y in range(len(board)):
                if board[y][x] != -1:
                    bingoChance = False
                    break
            if bingoChance == True:
                bingo = True
                break

    return bingo


def sum_unmarked(board):
    sum = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != -1:
                sum += board[y][x]

    return sum


firstResult = -1
lastResult = -1
for number in drawnNumbers:
    mark_number(boards, number)

    for board in boards:
        if check_for_bingo(board) == True:
            if firstResult == -1:
                firstResult = sum_unmarked(board) * number
            elif len(boards) == 1:
                lastResult = sum_unmarked(board) * number
            boards.remove(board)

    if len(boards) == 0:
        break

print(f"4-1: {firstResult}")
print(f"4-2: {lastResult}")
