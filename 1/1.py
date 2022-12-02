#!/usr/bin/env python3
file1 = '1.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
n = [0]
m = 0
for v in input:
    if len(v) > 0:
        n[m] += int(v) 
    else:
        m += 1
        n.append(0)
n.sort()
print(n[-1])
print(sum(n[-3:]))