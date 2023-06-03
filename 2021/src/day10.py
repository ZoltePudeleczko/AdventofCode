with open('./inputs/day10.txt') as f:
    subsystem = [line.strip() for line in f.readlines()]

matcher = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

points = {
    "(": 1,
    ")": 3,
    "[": 2,
    "]": 57,
    "{": 3,
    "}": 1197,
    "<": 4,
    ">": 25137,
}

completeScores = []
errorScore = 0
for line in subsystem:
    isCorrupted = False
    openingCharacters = []

    for character in line:
        if character in matcher:
            openingCharacters += character
        elif character in matcher.values():
            if character != matcher[openingCharacters[-1]]:
                isCorrupted = True
                errorScore += points[character]
                break
            else:
                openingCharacters.pop()
    
    if not isCorrupted:
        openingCharacters.reverse()
        score = 0
        for character in openingCharacters:
            score *= 5
            score += points[character]
        completeScores.append(score)

completeScores.sort()

print(f"10-1: {errorScore}")
print(f"10-2: {completeScores[len(completeScores)//2]}")
