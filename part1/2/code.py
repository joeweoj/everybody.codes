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

total = 0
# Split the line into chunks of 2 characters
for i in range(0, len(line), 2):
    chunk = line[i:i+2]
    additional = 0 if 'x' in chunk else 1
    c1 = index[chunk[0]] + additional
    c2 = index[chunk[1]] + additional
    cTotal = c1 + c2

    print (f'chunk={chunk},c1={c1}, c2={c2}, cTotal={cTotal}, additional={additional}')
    total += cTotal

print (f'total={total}')