with open('../inputs/day21.txt') as f:
    products = []
    for line in f.readlines():
        line = line.strip()
        products.append([line[:line.index('(') - 1].split(' '), line[line.index('(') + 10:-1].replace(',', '').split(' ')])

possibleCombo = {}
for product in products:
    for allergen in product[1]:
        if allergen not in possibleCombo.keys():
            possibleCombo[allergen] = product[0]
        else:
            possibleCombo[allergen] = [p for p in possibleCombo[allergen] if p in product[0]]
dangerousIngredients = []
for allergen in possibleCombo.keys():
    for ingredient in possibleCombo[allergen]:
        if ingredient not in dangerousIngredients:
            dangerousIngredients.append(ingredient)

result = 0
for product in products:
    for ingredient in product[0]:
        if ingredient not in dangerousIngredients:
            result += 1

print(f"21-1: {result}")


def use_allergen(comb):
    return comb[0]


change = 1
while change:
    change = 0
    foundIngredients = []
    for allergen in possibleCombo.keys():
        if len(possibleCombo[allergen]) == 1:
            foundIngredients.append(possibleCombo[allergen][0])
    for allergen in possibleCombo.keys():
        if len(possibleCombo[allergen]) > 1:
            possibleCombo[allergen] = [i for i in possibleCombo[allergen] if i not in foundIngredients]
            change = 1

dangerousComboList = []
for allergen in possibleCombo.keys():
    dangerousComboList.append((allergen, possibleCombo[allergen][0]))
dangerousComboList.sort(key=use_allergen)

result = ""
for comb in dangerousComboList:
    result += f",{comb[1]}"
result = result[1:]

print(f"21-2: {result}")
