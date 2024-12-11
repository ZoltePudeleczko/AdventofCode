from common import *

DAY_NUMBER = 11
USE_EXAMPLE = False


with get_data(DAY_NUMBER, USE_EXAMPLE) as f:
    starting_stones = [int(i) for i in f.readline().strip().split()]
    stones_count = {}
    for i in starting_stones:
        stones_count[i] = stones_count.get(i, 0) + 1


def blink(stones):
    new_stones = {}
    for key, value in stones.items():
        if key == 0:
            new_stones[1] = new_stones.get(1, 0) + value
        elif len(str(key)) % 2 == 0:
            left = int(str(key)[: len(str(key)) // 2])
            right = int(str(key)[len(str(key)) // 2 :])
            new_stones[left] = new_stones.get(left, 0) + value
            new_stones[right] = new_stones.get(right, 0) + value
        else:
            new_stones[key * 2024] = new_stones.get(key * 2024, 0) + value

    return new_stones


def part_one():
    stones = stones_count.copy()
    for _ in range(25):
        stones = blink(stones)

    return sum(stones.values())


def part_two():
    stones = stones_count.copy()
    for _ in range(75):
        stones = blink(stones)

    return sum(stones.values())


print_result(DAY_NUMBER, 1, part_one())
print_result(DAY_NUMBER, 2, part_two())
