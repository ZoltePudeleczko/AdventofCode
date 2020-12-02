with open('inputs/day1.txt') as f:
    expenses = [int(line) for line in f.readlines()]

for i in range(len(expenses)):
    for j in range(i+1, len(expenses)):
        if expenses[i] + expenses[j] == 2020:
            print(f"1-1: {expenses[i] * expenses[j]}")

for i in range(len(expenses)):
    for j in range(i+1, len(expenses)):
        for k in range(j+1, len(expenses)):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                print(f"1-2: {expenses[i] * expenses[j] * expenses[k]}")