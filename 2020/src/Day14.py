def use_mask(mask, value):
    value = list(format(value, f"0{len(mask) - 1}b"))
    for i in range(len(mask)):
        if mask[i] == '0' and value[i] == '1':
            value[i] = '0'
        elif mask[i] == '1' and value[i] == '0':
            value[i] = '1'
    return int(''.join(value), 2)


def use_mask2(mask, address):
    address = list(format(address, f"0{len(mask) - 1}b"))
    addresses = [address]
    for i in range(len(mask)):
        if mask[i] == '1' and address[i] == '0':
            for a in addresses:
                a[i] = '1'
        elif mask[i] == 'X':
            newAddresses = []
            for a in addresses:
                tAddress = a.copy()
                tAddress[i] = '0'
                newAddresses.append(tAddress)
                tAddress = a.copy()
                tAddress[i] = '1'
                newAddresses.append(tAddress)
            addresses.extend(newAddresses)
    for i in range(len(addresses)):
        addresses[i] = int(''.join(addresses[i]))
    return addresses


with open('../inputs/day14.txt') as f:
    lines = f.readlines()

memory = {}
for line in lines:
    if line[:4] == 'mask':
        mask = line[7:]
    else:
        address = int(line[line.index('[') + 1:line.index(']')])
        value = use_mask(mask, int(line[line.index('=') + 2:]))
        memory[address] = value

print(f"14-1: {sum(memory.values())}")

memory = {}
for line in lines:
    if line[:4] == 'mask':
        mask = line[7:]
    else:
        address = int(line[line.index('[') + 1:line.index(']')])
        addresses = use_mask2(mask, address)
        value = int(line[line.index('=') + 2:])
        for a in addresses:
            memory[a] = value

print(f"14-2: {sum(memory.values())}")
