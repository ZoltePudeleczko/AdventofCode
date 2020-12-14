with open('../inputs/day13.txt') as f:
    lines = f.readlines()
    myTimestamp = int(lines[0])
    allBusses = lines[1].strip()

busses = [int(bus) for bus in allBusses.replace(',x', '').split(',')]
departings = []
closest = None
for bus in busses:
    time = bus
    while time < myTimestamp:
        time += bus
    departings.append((bus, time - myTimestamp))
    if closest is None or closest[1] > time - myTimestamp:
        closest = (bus, time - myTimestamp)

print(f"13-1: {closest[0] * closest[1]}")

# What time is it? It's Chinese Remainder Theorem time!
allBusses = allBusses.split(',')
values = []
mods = []
skipValue = 0
for bus in allBusses:
    if bus != 'x':
        values.append(int(bus))
        mods.append(abs((int(bus) - skipValue) % int(bus)))
    skipValue += 1

N = 1
for v in values:
    N *= v

x = 0
for v, m in zip(values, mods):
    x += m * (N // v) * pow(N // v, -1, v)
x %= N

print(f"13-2: {x}")
