with open('../inputs/day6.txt') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]

sum = 0
questions = []
for l in lines:
    if l is '':
        sum += len(questions)
        questions = []
        continue

    for c in l:
        if c not in questions:
            questions.append(c)
sum += len(questions)

print(f"6-1: {sum}")

sum = 0
newGroup = 1
questions = []
for l in lines:
    if l is '':
        sum += len(questions)
        questions = []
        newGroup = 1
        continue

    if newGroup == 1:
        for c in l:
            questions.append(c)
        newGroup = 0
    else:
        questionstemp = questions.copy()
        for c in questionstemp:
            if c not in l:
                questions.remove(c)
sum += len(questions)

print(f"6-2: {sum}")
