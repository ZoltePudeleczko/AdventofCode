with open('inputs/day10.txt') as f:
    jolts = [int(line) for line in f.readlines()]

jolts.append(max(jolts) + 3)
jolts.sort()

currentJolts = 0
differences = [0, 0, 0]
for adapter in jolts:
    differences[adapter - currentJolts - 1] += 1
    currentJolts = adapter

print(f"10-1: {differences[0] * differences[2]}")

arrangements = {
    0: 1
}
for adapter in jolts:
    if adapter not in arrangements.keys():
        arrangements[adapter] = 0

    if adapter - 1 in arrangements.keys():
        arrangements[adapter] += arrangements[adapter - 1]
    if adapter - 2 in arrangements.keys():
        arrangements[adapter] += arrangements[adapter - 2]
    if adapter - 3 in arrangements.keys():
        arrangements[adapter] += arrangements[adapter - 3]

print(f"10-2: {arrangements[max(jolts)]}")
