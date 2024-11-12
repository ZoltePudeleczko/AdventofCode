with open("../inputs/day8.txt") as f:
    inputs = [
        [digits[:10], digits[10:]]
        for digits in [line.strip().replace("|", "").split() for line in f.readlines()]
    ]

uniqueLengthsToDigits = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}


def workout_segments(input):
    dictionary = {}

    for i in range(len(input)):  # 1, 4, 7, 8 have unique lengths
        if len(input[i]) in uniqueLengthsToDigits.keys():
            dictionary[uniqueLengthsToDigits[len(input[i])]] = input[i]

    for i in range(len(input)):  # 3, 6, 9 are kinda tricky
        if input[i] not in dictionary.values():
            if len(input[i]) == 5 and all(
                letter in set(input[i]) for letter in dictionary[1]
            ):  # 3 includes 1 (2, 5 don't)
                dictionary[3] = input[i]
            elif len(input[i]) == 6 and not all(
                letter in set(input[i]) for letter in dictionary[1]
            ):  # 6 does NOT include 1 (but 0 and 9 do)
                dictionary[6] = input[i]
            elif len(input[i]) == 6 and all(
                letter in set(input[i]) for letter in dictionary[4]
            ):  # 9 includes 4 (0 and 6 don't)
                dictionary[9] = input[i]

    for i in range(len(input)):  # 0, 2, 5 are just tricky
        if input[i] not in dictionary.values():
            if len(input[i]) == 6:  # 0 is the only left with 6 characters
                dictionary[0] = input[i]
            elif (
                len(input[i]) == 5
                and len(
                    [letter for letter in dictionary[6] if letter not in set(input[i])]
                )
                == 1
            ):  # 5 does NOT include 1 character from 6
                dictionary[5] = input[i]
            elif (
                len(input[i]) == 5
                and len(
                    [letter for letter in dictionary[6] if letter not in set(input[i])]
                )
                == 2
            ):  # 2 does NOT include 2 characters from 6 (did I mention I'm desperate?)
                dictionary[2] = input[i]

    return {v: k for k, v in dictionary.items()}


def decode_output(input):
    dictionary = workout_segments(input[0])

    output = ""
    for out in input[1]:
        for key in dictionary.keys():
            if len(out) == len(key) and all(letter in set(out) for letter in key):
                output += str(dictionary[key])
                break

    return int(output)


count = 0
for input in inputs:
    count += len([d for d in input[1] if len(d) in uniqueLengthsToDigits.keys()])

print(f"8-1: {count}")

outputsSum = 0
for input in inputs:
    outputsSum += decode_output(input)

print(f"8-2: {outputsSum}")
