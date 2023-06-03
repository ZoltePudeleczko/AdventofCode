with open('../inputs/day4.txt') as f:
    passportsLines = [line.replace('\n', '').replace(':', ' ').split(' ') for line in f.readlines()]

passportsData = []
for line in passportsLines:
    passportsData.extend(line)

passports = [{}]
i = 0
while i < len(passportsData):
    if passportsData[i] is '':
        passports.append({})
        i += 1
        continue
    passports[len(passports) - 1][passportsData[i]] = passportsData[i + 1]
    i += 2

valid = 0
for p in passports:
    if ('byr' in p
        and 'iyr' in p
        and 'eyr' in p
        and 'hgt' in p
        and 'hcl' in p
        and 'ecl' in p
        and 'pid' in p
    ):
        valid += 1

print(f"4-1: {valid}")

valid = 0
for p in passports:
    if ('byr' in p
        and 'iyr' in p
        and 'eyr' in p
        and 'hgt' in p
        and 'hcl' in p
        and 'ecl' in p
        and 'pid' in p
    ):
        if 1920 <= int(p['byr']) <= 2002:
            if 2010 <= int(p['iyr']) <= 2020:
                if 2020 <= int(p['eyr']) <= 2030:
                    if p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        if p['pid'].isdigit() and len(p['pid']) == 9:
                            if len(p['hcl']) == 7 and p['hcl'][0] == '#':
                                for c in p['hcl'][1:]:
                                    if ord(c) not in range(ord('0'), ord('9')) and ord(c) not in range(ord('a'), ord('f')):
                                        continue
                                if len(p['hgt']) == 5 and p['hgt'][-2:] == 'cm':
                                    if 150 <= int(p['hgt'][:3]) <= 193:
                                        valid += 1
                                elif len(p['hgt']) == 4 and p['hgt'][-2:] == 'in':
                                    if 59 <= int(p['hgt'][:2]) <= 76:
                                        valid += 1

print(f"4-2: {valid}")