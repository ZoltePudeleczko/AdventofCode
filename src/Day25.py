def transform_subject(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value


def find_loop_size(subject_number, public_key):
    value = 1
    loop = 0
    while value != public_key:
        loop += 1
        value *= subject_number
        value %= 20201227
    return loop


with open('../inputs/day25.txt') as f:
    doorPublicKey = int(f.readline().strip())
    cardPublicKey = int(f.readline().strip())

print(transform_subject(doorPublicKey, find_loop_size(7, cardPublicKey)))
