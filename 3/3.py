#!/usr/bin/env python3
file1 = '3.in'


def score_of_chars(c):
    v = ord(c)
    if v < 96:
        r = v - 64 + 26
    elif v > 96:
        r = v - 96
    return r

input = [x.strip() for x in open(file1, 'r').readlines()]
score = 0
score2 = 0
badges = set()
c = 0


for v in input:
    if c % 3 == 0:
        if len(badges) > 0:
            score2 += score_of_chars(badges.pop())
        badges = set(v)
        print(v, badges)
        c = 0
    else:
        badges = badges.intersection(set(v))
    c += 1
    # print(score2, badges)

    sp = int(len(v)/2)
    p1 = v[0:sp]
    p2 = v[sp:]
    
    m = set()

    

    for x in p1:
        if x in p2:
            m.add(x)
    for x in m:
        score += score_of_chars(x)

        # print(x, r)

score2 += score_of_chars(badges.pop())
print(score)
print(score2)

    # print(m)