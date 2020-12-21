import re


def rule_expand(rules, cur_rule):
    if cur_rule.isalpha():
        return cur_rule
    elif mo := re.match(r'^\d+$', cur_rule):
        return f"{rule_expand(rules, rules[cur_rule])}"
    elif mo := re.search(r'^(.*?).[|].(.*?)$', cur_rule):
        return f"{rule_expand(rules, mo.group(1))}|{rule_expand(rules, mo.group(2))}"
    elif mo := re.findall(r'(\d+)', cur_rule):
        output = ""
        for res in mo:
            output += f"({rule_expand(rules, res)})"
        return output


def rule_expand_stop(rules, cur_rule, maxLength, length=0):
    if length > maxLength:
        return ""

    if cur_rule.isalpha():
        return cur_rule
    elif mo := re.match(r'^\d+$', cur_rule):
        return f"{rule_expand_stop(rules, rules[cur_rule], maxLength, length + 1)}"
    elif mo := re.search(r'^(.*?).[|].(.*?)$', cur_rule):
        return f"{rule_expand_stop(rules, mo.group(1), maxLength, length + 1)}|{rule_expand_stop(rules, mo.group(2), maxLength, length + 1)}"
    elif mo := re.findall(r'(\d+)', cur_rule):
        output = ""
        for res in mo:
            output += f"({rule_expand_stop(rules, res, maxLength, length + 1)})"
        return output


with open('../inputs/day19.txt') as f:
    rules = {}
    lines = f.readlines()
    i = 0
    while lines[i] != '\n':
        line = lines[i].strip().replace(':', '').replace('"', '')
        rules[line[:line.index(' ')]] = line[line.index(' ') + 1:]
        i += 1
    words = []
    for line in lines[i + 1:]:
        words.append(line.strip())
        i += 1

validRule = f"^{rule_expand(rules, rules['0'])}$"
valid = 0
for word in words:
    if re.search(validRule, word):
        valid += 1

print(f"19-1: {valid}")

rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

maxWordLength = max(len(word) for word in words)
validRule2 = f"^{rule_expand_stop(rules, rules['0'], maxWordLength)}$"

valid = 0
for word in words:
    if re.search(validRule2, word):
        valid += 1

print(f"19-2: {valid}")
