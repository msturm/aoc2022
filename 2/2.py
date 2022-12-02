#!/usr/bin/env python3
file1 = '2.in'

score = 0 
score2 = 0

input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    p, q = [x.strip() for x in v.split()]
    if p == 'A':
        if q == 'X':
            score += 1 + 3
            score2 += 3 + 0
        elif q == 'Y':
            score += 2 + 6
            score2 += 1 + 3
        elif q == 'Z':
            score += 3 + 0
            score2 += 2 + 6
    elif p == 'B':
        if q == 'X':
            score += 1 + 0
            score2 += 1 + 0
        elif q == 'Y':
            score += 2 + 3
            score2 += 2 + 3
        elif q == 'Z':
            score += 3 + 6
            score2 += 3 + 6
    elif p == 'C':
        if q == 'X':
            score += 1 + 6
            score2 += 2 + 0
        elif q == 'Y':
            score += 2 + 0
            score2 += 3 + 3
        elif q == 'Z':
            score += 3 + 3
            score2 += 1 + 6

print(score)
print(score2)