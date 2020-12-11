with open('inputs/day2.txt') as f:
    passwordlines = [line.split() for line in [r.replace('-', ' ').replace(':', '') for r in f.readlines()]]

valid = 0
for password in passwordlines:
    if int(password[0]) <= password[3].count(password[2]) <= int(password[1]):
        valid += 1

print(f"2-1: {valid}")

valid = 0
for password in passwordlines:
    if password[3][int(password[0]) - 1] == password[2]:
        if password[3][int(password[1]) - 1] != password[2]:
            valid += 1
    else:
        if password[3][int(password[1]) - 1] == password[2]:
            valid += 1

print(f"2-2: {valid}")