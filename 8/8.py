#!/usr/bin/env python3
file1 = '8.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
G = {}

for r, v in enumerate(input):
    for c in range(0, len(v)):
        G[(r, c)] = int(v[c])

max_c = len(v)
max_r = len(input)
visible = 0
max_sc = 0

for r in range(0, max_c):
    for c in range(0, max_r):
        cv = G[(r, c)]
       
        if (all([G[(dr, c)] < cv for dr in range(0, r)]) or
                all([G[(dr, c)] < cv for dr in range(r+1, max_r)]) or
                all([G[(r, dc)] < cv for dc in range(0, c)]) or 
                all([G[(r, dc)] < cv for dc in range(c+1, max_c)])):
            visible += 1


        if r > 0 and r < max_r - 1 and  c > 0 and c < max_c - 1:
            # calculate scenic score
            sc = 0
            vis = True
            d = 1 

            while r - d > 0 and G[(r - d, c)] < cv:
                d += 1
            sc = d

            d = 1
            while r + d < max_r - 1 and G[(r + d, c)] < cv:
                d += 1
            sc *= d

            d = 1
            while c - d > 0 and G[(r, c - d)] < cv:
                d += 1
            sc *= d

            d = 1
            while c + d < max_c - 1 and G[(r, c + d)] < cv:
                d += 1
            sc *= d
          
            max_sc = max(sc, max_sc)

print("part1", visible)
print("part2", max_sc)