#!/usr/bin/env python3
file1 = '18.in'
from collections import deque
G = set()

input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    x, y, z = [int(x) for x in v.split(',')]
    G.add((x, y, z))

D = {(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)}
AB = set()
size_covered = 0
for (x, y, z) in G:
    for (dx, dy, dz) in D:
        if (x+dx,y+dy,z+dz) in G:
            size_covered += 1
        else:
            AB.add((x+dx,y+dy,z+dz))


part1 = (len(G)*6)-size_covered
print("part1", part1)

airdrops = set()
INSIDE=set()
OUTSIDE=set()


def is_inside(x, y, z):
    if (x, y, z) in INSIDE:
        return True
    if (x, y, z) in OUTSIDE:
        return False
    CHECKED = set()
    Q = deque([(x, y, z)])
    while Q:
        # print(len(CHECKED))
        (cx, cy, cz) = Q.popleft()
        if (cx, cy, cz) in CHECKED:
            continue
        CHECKED.add((cx, cy, cz))
        if len(CHECKED) > 4000:
            for p in CHECKED:
                OUTSIDE.add((x, y, z))
            return False
        if (cx, cy, cz) not in G:
            for (dx, dy, dz) in D:
                Q.append((cx+dx,cy+dy,cz+dz))
    for p in CHECKED:
        INSIDE.add(p)
    return True


part2 = 0
for (x, y, z) in G:
    for (dx, dy, dz) in D:
        if not is_inside(x+dx,y+dy,z+dz):
            part2 += 1

print("part 2", part2)