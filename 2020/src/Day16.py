with open('../inputs/day16.txt') as f:
    fields = []
    line = f.readline()
    # fields initialization
    while line != '\n':
        firstValue = int(line[line.index(':') + 2:line.index('-')])
        secondValue = int(line[line.index('-') + 1:line.index(' or ')])
        thirdValue = int(line[line.index(' or ') + 4:line[line.index(' or '):].index('-') + line.index(' or ')])
        fourthValue = int(line[line[line.index(' or '):].index('-') + line.index(' or ') + 1:])
        fields.append([(firstValue, secondValue), (thirdValue, fourthValue)])
        line = f.readline()
    
    # my ticket
    f.readline()
    myTicket = [int(value) for value in f.readline().strip().split(',')]
    
    # other tickets
    f.readline()
    f.readline()
    tickets = []
    line = f.readline()
    while line != '':
        tickets.append([int(value) for value in line.strip().split(',')])
        line = f.readline()

validTickets = [myTicket]
wrongValuesSum = 0
for ticket in tickets:
    isTicketValid = 1
    for value in ticket:
        valid = 0
        for field in fields:
            if (field[0][0] <= value <= field[0][1]) or (field[1][0] <= value <= field[1][1]):
                valid = 1
                break
        if valid == 0:
            isTicketValid = 0
            wrongValuesSum += value
    if isTicketValid:
        validTickets.append(ticket)

print(f"16-1: {wrongValuesSum}")

valuesToFields = [list(range(len(fields))) for f in fields]
for ticket in validTickets:
    for i in range(len(ticket)):
        fieldsToRemove = []
        for possibleFieldIndex in valuesToFields[i]:
            if (fields[possibleFieldIndex][0][0] <= ticket[i] <= fields[possibleFieldIndex][0][1]) or (fields[possibleFieldIndex][1][0] <= ticket[i] <= fields[possibleFieldIndex][1][1]):
                continue
            else:
                fieldsToRemove.append(possibleFieldIndex)
        valuesToFields[i] = [f for f in valuesToFields[i] if f not in fieldsToRemove]

foundFields = []
change = 1
while change:
    change = 0
    for field in valuesToFields:
        if len(field) == 1 and field[0] not in foundFields:
            change = 1
            foundFields.append(field[0])
    for i in range(len(valuesToFields)):
        if len(valuesToFields[i]) > 1:
            valuesToFields[i] = [f for f in valuesToFields[i] if f not in foundFields]

departureMultiplied = 1
for i in range(len(valuesToFields)):
    if valuesToFields[i][0] < 6:
        departureMultiplied *= myTicket[i]

print(f"16-2: {departureMultiplied}")
