with open("../inputs/day6.txt") as f:
    fish = [int(n) for n in f.readline().strip().split(",")]


def simulate_lanternfish(fish, days):
    fishCount = [0] * 9
    for f in fish:
        fishCount[f] += 1

    for i in range(days):
        tempFish = fishCount[8]
        for fishIndex in range(len(fishCount), 0, -1):
            fishCount[fishIndex - 1], tempFish = tempFish, fishCount[fishIndex - 1]
        fishCount[8] = tempFish
        fishCount[6] += tempFish
    return sum(fishCount)


print(f"6-1: {simulate_lanternfish(fish[:], 80)}")
print(f"6-2: {simulate_lanternfish(fish[:], 256)}")
