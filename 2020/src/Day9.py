with open('../inputs/day9.txt') as f:
    numbers = [int(line) for line in f.readlines()]

preamble = []
iter = 0
invalidNumber = -1
for number in numbers:
    if len(preamble) < 25:
        preamble.append(number)
    else:
        summable = 0
        for i in range(len(preamble)):
            for j in range(i + 1, len(preamble)):
                if preamble[i] + preamble[j] == number:
                    summable = 1
                    break
            if summable == 1:
                break
        if summable == 1:
            preamble[iter] = number
            iter = (iter + 1) % len(preamble)
        else:
            invalidNumber = number
            break

print(f"9-1: {invalidNumber}")

encryptionWeakness = -1
for i in range(len(numbers)):
    sum = numbers[i]
    for j in range(i + 1, len(numbers)):
        sum += numbers[j]
        if sum > invalidNumber:
            break
        elif sum == invalidNumber:
            encryptionWeakness = min(numbers[i:j]) + max(numbers[i:j])
    if encryptionWeakness != -1:
        break

print(f"9-2: {encryptionWeakness}")
