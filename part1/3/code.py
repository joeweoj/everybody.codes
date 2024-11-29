#! /usr/bin/env python3


f = open('source.txt')
line = f.read()
index = {
    'A': 0,
    'B': 1,
    'C': 3,
    'D': 5,
    'x': 0
}
additionalFactor = {
    0: 2,
    1: 1,
    2: 0
}

def get_positions_per_creature(key):
    if key == 'x':
        return 0
    additional = 2 - chunk.count('x')
    return index[key] + additional


total = 0
# Split the line into chunks of 2 characters
for i in range(0, len(line), 3):
    chunk = line[i:i+3]
    
    c1 = get_positions_per_creature(chunk[0])
    c2 = get_positions_per_creature(chunk[1])
    c3 = get_positions_per_creature(chunk[2])
    cTotal = c1 + c2 + c3

    print (f'chunk={chunk},c1={c1}, c2={c2}, c3={c3}, cTotal={cTotal}')
    total += cTotal

print (f'total={total}')