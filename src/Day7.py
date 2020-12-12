with open('../inputs/day7.txt') as f:
    rules = [line.replace('bags', '')
             .replace('bag', '')
             .replace('contain', '')
             .replace(',', '')
             .replace('.', '').split() for line in f.readlines()]

rulesBook = {}
for rule in rules:
    key = rule[0] + ' ' + rule[1]
    if len(rule) == 4:
        rulesBook[key] = []
        continue
    contains = []
    for i in range(2, len(rule), 3):
        contains.append((int(rule[i]), rule[i + 1] + ' ' + rule[i + 2]))
    rulesBook[key] = contains

lookingFor = ['shiny gold']
validBags = []
changed = 1
while changed == 1:
    changed = 0
    for key in rulesBook.keys():
        if key in lookingFor:
            continue
        for contains in rulesBook[key]:
            if contains[1] in lookingFor:
                if key not in validBags:
                    validBags.append(key)
                lookingFor.append(key)
                changed = 1

print(f"7-1: {len(validBags)}")

lookingFor = [(1, 'shiny gold')]
bagsCount = 0
while len(lookingFor) > 0:
    changed = 0
    newLookingFor = []
    for key in lookingFor:
        for contains in rulesBook[key[1]]:
            newLookingFor.append((contains[0] * key[0], contains[1]))
            bagsCount += contains[0] * key[0]
    lookingFor = newLookingFor.copy()

print(f"7-2: {bagsCount}")