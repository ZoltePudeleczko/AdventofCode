def calculate_bracket(expression, startIndex = 0):
    leftValue = -1
    symbol = None
    i = startIndex
    while i < len(expression):
        if expression[i].isdigit():
            if leftValue == -1:
                leftValue = int(expression[i])
            else:
                if symbol == '+':
                    leftValue += int(expression[i])
                elif symbol == '*':
                    leftValue *= int(expression[i])
        else:
            if expression[i] in ['+', '*']:
                symbol = expression[i]
            elif expression[i] == '(':
                calculate = calculate_bracket(expression, i + 1)
                i = calculate[1]
                if symbol is None:
                    leftValue = calculate[0]
                elif symbol == '+':
                    leftValue += calculate[0]
                elif symbol == '*':
                    leftValue *= calculate[0]
            elif expression[i] == ')':
                return (leftValue, i)
        i += 1
    return leftValue


def put_brackets_addition(expression):
    i = 0
    while '+' in expression[i:]:
        index = expression[i:].index('+') + i
        bracketsCount = 0
        for x in range(index - 1, -1, -1):
            if expression[x].isdigit() and bracketsCount == 0:
                expression.insert(x, '(')
                break
            elif expression[x] == ')':
                bracketsCount += 1
            elif expression[x] == '(':
                bracketsCount -= 1
                if bracketsCount == 0:
                    expression.insert(x, '(')
                    break
        bracketsCount = 0
        for x in range(index + 1, len(expression)):
            if expression[x].isdigit() and bracketsCount == 0:
                expression.insert(x + 1, ')')
                break
            elif expression[x] == '(':
                bracketsCount += 1
            elif expression[x] == ')':
                bracketsCount -= 1
                if bracketsCount == 0:
                    expression.insert(x, ')')
                    break
        i = index + 2
    return expression


with open('../inputs/day18.txt') as f:
    expressions = [n.strip().replace('(', '( ').replace(')', ' )').split(' ') for n in f.readlines()]

expressionsSum = 0
expressionsSum2 = 0
for expression in expressions:
    expressionsSum += calculate_bracket(expression)
    expressionsSum2 += calculate_bracket(put_brackets_addition(expression))

print(f"18-1: {expressionsSum}")
print(f"18-2: {expressionsSum2}")
