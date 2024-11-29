#! /usr/bin/env python3

f = open('source.txt')
line = f.read()
index = {
    'A': 0,
    'B': 1,
    'C': 3
}

total = 0;
for s in line:
    total += index[s]

print (f'total={total}')