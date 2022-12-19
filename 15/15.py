#!/usr/bin/env python3
# file1 = '15.test'
file1 = '15.in'
from copy import deepcopy
input = [x.strip() for x in open(file1, 'r').readlines()]
G = set()

B = set()
max_x = 0
min_x = 0
for v in input:
    words = v.split()
    sx = words[2].split('=')[1][0:-1]
    sy = words[3].split('=')[1][0:-1]
    bx = words[-2].split('=')[1][0:-1]
    by = words[-1].split('=')[1]
    bx, by, sx, sy = int(bx), int(by), int(sx), int(sy)
    G.add((sx, sy, abs(bx - sx) + abs(by - sy)))
    B.add((bx, by))
    max_x = max(max_x, (sx + abs(bx - sx) + abs(by - sy)))
    min_x = min(min_x, (sx - abs(bx - sx) + abs(by - sy)))
    # print(bx, by, sx, sy)
    # print(G)


# [print(x, G[x]) for x in G]
# y = 1
y = 2000000
blocked = set()
for (sx, sy, d) in G:
    if d >= abs(y-sy):
        r = d - abs(y-sy)
        for xx in range(-r, r+1): 
            if (sx+xx, y) not in B:
                blocked.add((sx + xx, y))

print("p1", len(blocked))
# max_range = 20
max_range = 4000000

def valid(x, y, G):
    if not (0 <= x <= max_range and 0 <= y <= max_range):
        return False
    for sx, sy, d in G:
        dxy = abs(sx - x) + abs(sy - y)
        if d >= dxy:
            return False
    return True

points_to_check = set()
counter = 0
p2 = 0
for (sx, sy, d) in G:
    mhd = d + 1
    for dd in range(0, mhd):
        new_points = [(sx + mhd - dd, sy + dd),
            (sx - mhd + dd, sy + dd),
            (sx + dd, sy + mhd - dd),
            (sx + dd, sy - mhd + dd)]
        for np in new_points:
            counter += 1
            if counter % 500000 == 0:
                print('.', end='')
            np_x, np_y = np
            if valid(np_x, np_y, G):
                p2 = np_x * 4000000 + np_y
                print(p2)
                assert(False)

print("p2", p2 )
