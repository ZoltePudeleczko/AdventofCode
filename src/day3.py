with open('./inputs/day3.txt') as f:
    numbers = [line.strip() for line in f.readlines()]

def common_count(numbers):
    commonCount = [0] * len(numbers[0])
    for n in numbers:
        for i in range(len(n)):
            if (n[i] == '1'):
                commonCount[i] += 1
            else:
                commonCount[i] -= 1
    return commonCount

commonCount = common_count(numbers)

gammaRate = ''
epsilonRate = ''
for n in commonCount:
    if n < 0:
        gammaRate += '0'
        epsilonRate += '1'
    else:
        gammaRate += '1'
        epsilonRate += '0'

print(f"2-1: {gammaRate} {epsilonRate} {int(gammaRate, 2) * int(epsilonRate, 2)}")

generatorRatings = numbers[:]
scrubberRatings = numbers[:]

i = 0
while len(generatorRatings) > 1:
    commonCount = common_count(generatorRatings)
    if commonCount[i] >= 0:
        generatorRatings = [r for r in generatorRatings if r[i] == '1']
    else:
        generatorRatings = [r for r in generatorRatings if r[i] == '0']
    i += 1

i = 0
while len(scrubberRatings) > 1:
    commonCount = common_count(scrubberRatings)
    if commonCount[i] >= 0:
        scrubberRatings = [r for r in scrubberRatings if r[i] == '0']
    else:
        scrubberRatings = [r for r in scrubberRatings if r[i] == '1']
    i += 1 

print(f"2-2: {generatorRatings[0]} {scrubberRatings[0]} {int(generatorRatings[0], 2) * int(scrubberRatings[0], 2)}")
