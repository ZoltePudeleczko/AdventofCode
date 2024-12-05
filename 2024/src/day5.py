from common import *

DAY_NUMBER = 5
USE_EXAMPLE = False


def check_is_valid(update):
    for i in range(len(update)):
        if not_allowed_after.get(update[i]) is None:
            continue

        if any(v in not_allowed_after[update[i]] for v in update[i:]):
            return (update, False)

    return (update, True)


with get_data(DAY_NUMBER, USE_EXAMPLE) as f:
    not_allowed_after = dict()
    while True:
        l = f.readline().strip()
        if l == "":
            break

        parts = l.split("|")
        if not_allowed_after.get(parts[1]) is None:
            not_allowed_after[parts[1]] = [parts[0]]
        else:
            not_allowed_after[parts[1]].append(parts[0])

    updates = [check_is_valid(l.strip().split(",")) for l in f.readlines()]


def get_middle_value(update):
    return int(update[int((len(update) - 1) / 2)])


def fix_update(update):
    i = 0
    while i < len(update):
        if not_allowed_after.get(update[i]) is None:
            i += 1
            continue

        for j in range(i + 1, len(update)):
            if update[j] in not_allowed_after[update[i]]:
                moved = update.pop(j)
                update.insert(i, moved)
                i -= 1
                break

        i += 1

    return update


def part_one():
    return sum([get_middle_value(update[0]) for update in updates if update[1]])


def part_two():
    return sum(
        [get_middle_value(fix_update(update[0])) for update in updates if not update[1]]
    )


print_result(DAY_NUMBER, 1, part_one())
print_result(DAY_NUMBER, 2, part_two())
