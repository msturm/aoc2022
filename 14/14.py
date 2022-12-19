#!/usr/bin/env python3
from copy import deepcopy
file1 = '14.in'

G = {}
max_y = 0
input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    D = [(int(u), int(v)) for u, v in [y.split(',') for y  in [x.strip() for x in v.split('->')]]]
    E = [(p1, p2) for p1, p2 in zip(D[0:-1], D[1:])]
    for p1, p2 in E:
        xmin = p1[0] if p1[0] <= p2[0] else p2[0]
        xmax = p2[0] if p1[0] <= p2[0] else p1[0]
        ymin = p1[1] if p1[1] <= p2[1] else p2[1]
        ymax = p2[1] if p1[1] <= p2[1] else p1[1]

        for x1 in range(xmin, xmax + 1):
            for y1 in range(ymin, ymax + 1):
                G[(x1, y1)] = '#'
        max_y = max(max_y, ymax)
print(sorted(G))

G1 = deepcopy(G)
unstable = True
s = (500, 0)
i = 0
while s[1] < max_y:
    sx, sy = s
    if (sx, sy + 1) not in G1:
        s = (sx, sy + 1)
    elif (sx - 1, sy + 1) not in G1:
        s = (sx - 1, sy + 1)
    elif (sx + 1, sy + 1) not in G1:
        s = (sx + 1, sy + 1)
    else:
        G1[(sx, sy)] = 'o'
        s = (500, 0)
        i += 1
    
print("p1", i)

# part 2

G2 = deepcopy(G)
unstable = True
s = (500, 0)
blocked = False
i = 0
while not blocked:
    sx, sy = s
    if sy == max_y + 1: # infinte floor
        G2[(sx, sy)] = 'o'
        s = (500, 0)
        i += 1
    elif (sx, sy + 1) not in G2:
        s = (sx, sy + 1)
    elif (sx - 1, sy + 1) not in G2:
        s = (sx - 1, sy + 1)
    elif (sx + 1, sy + 1) not in G2:
        s = (sx + 1, sy + 1)
    else:
        G2[(sx, sy)] = 'o'
        i += 1
        if (sx, sy) == (500, 0): # blocked
            break
        s = (500, 0)
print("p2", i)
        
