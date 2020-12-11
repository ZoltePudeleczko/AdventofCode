with open('inputs/day8.txt') as f:
    instructions = [line.split() for line in f.readlines()]

for instruction in instructions:
    instruction[1] = int(instruction[1])

index = 0
accumulator = 0
visited = []
while 1:
    if index in visited:
        break
    visited.append(index)

    if instructions[index][0] == 'nop':
        index += 1
        continue
    if instructions[index][0] == 'acc':
        accumulator += instructions[index][1]
        index += 1
        continue
    if instructions[index][0] == 'jmp':
        index += instructions[index][1]
        continue

print(f"8-1: {accumulator}")

for instruction in instructions:
    if instruction[1] == 0 or instruction[0] is 'acc':
        continue

    if instruction[0] == 'nop':
        instruction[0] = 'jmp'
    elif instruction[0] == 'jmp':
        instruction[0] = 'nop'

    index = 0
    accumulator = 0
    infinite = 0
    visited = []
    while index in range(len(instructions)):
        if index in visited:
            infinite = 1
            break
        visited.append(index)

        if instructions[index][0] == 'nop':
            index += 1
            continue
        if instructions[index][0] == 'acc':
            accumulator += instructions[index][1]
            index += 1
            continue
        if instructions[index][0] == 'jmp':
            index += instructions[index][1]
            continue

    if infinite == 0:
        break

    if instruction[0] == 'nop':
        instruction[0] = 'jmp'
    elif instruction[0] == 'jmp':
        instruction[0] = 'nop'

print(f"8-2: {accumulator}")