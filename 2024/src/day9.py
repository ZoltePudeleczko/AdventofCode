from common import *

DAY_NUMBER = 9
USE_EXAMPLE = False


with get_data(DAY_NUMBER, USE_EXAMPLE) as f:
    disk = [int(i) for i in f.readline().strip()]

    blocks = []
    is_file = True
    files_count = 0
    for i in disk:
        if is_file:
            blocks += [str(files_count)] * i
            files_count += 1
        else:
            blocks += ["."] * i
        is_file = not is_file


def find_first_free_space(blocks, length=1):
    for i in range(len(blocks) - length):
        if all([block == "." for block in blocks[i : i + length]]):
            return i
    return -1


def part_one():
    new_blocks = blocks.copy()
    for i in range(len(new_blocks) - 1, 0, -1):
        if new_blocks[i] == ".":
            continue

        free_ind = find_first_free_space(new_blocks[:i])
        if free_ind == -1:
            continue

        new_blocks[free_ind] = new_blocks[i]
        new_blocks[i] = "."

    return sum([i * int(block) for i, block in enumerate(new_blocks) if block != "."])


def part_two():
    new_blocks = blocks.copy()
    checked = []
    for i in range(len(new_blocks) - 1, 0, -1):
        if new_blocks[i] == ".":
            continue
        if new_blocks[i] in checked:
            continue

        checked.append(new_blocks[i])

        length = 1
        for j in range(i - 1, 0, -1):
            if new_blocks[j] == new_blocks[i]:
                length += 1
            else:
                break

        free_ind = find_first_free_space(new_blocks[:i], length)
        if free_ind == -1:
            continue

        for j in range(length):
            new_blocks[free_ind + j] = new_blocks[i - j]
            new_blocks[i - j] = "."

    return sum([i * int(block) for i, block in enumerate(new_blocks) if block != "."])


print_result(DAY_NUMBER, 1, part_one())
print_result(DAY_NUMBER, 2, part_two())
