#!/usr/bin/env python3
from collections import Counter
from copy import deepcopy
# file1 = '20.test'
file1 = '20.in'


def solve(n, key, O, D):
    zero_index = 0
    if key > 1:
        O = [(x, y*key) for x, y in O]
        D = O.copy()
    for _ in range(n):
        for (opos, x) in O:
            # print(O)
            
            i = D.index((opos, x))
            new_pos = (i+x) % (len(D) - 1)
            D.insert(new_pos, D.pop(i))

            print(i, x, i+x, new_pos)

            if x == 0:
                zero_index = opos
            
    ioz = D.index((zero_index, 0))
    print(ioz, D[ioz])
    return D[(ioz + 1000) % len(D)][1] + D[(ioz + 2000) % len(D)][1] + D[(ioz + 3000) % len(D)][1]


input = [x.strip() for x in open(file1, 'r').readlines()]
G = []

for v in input:
    G.append(int(v))

O = list(enumerate(G))
D = O.copy()



# print("duplicates", [v for v, x in Counter(O).items() if x > 1])
# print(O)
# print(D[(ioz + 1000) % len(D)], D[(ioz + 2000) % len(D)], D[(ioz + 3000) % len(D)])
# print(D[(ioz + 1000)], D[(ioz + 2000)], D[(ioz + 3000)])
# p1 = D[(ioz + 1000) % len(D)][1] + D[(ioz + 2000) % len(D)][1] + D[(ioz + 3000) % len(D)][1]
print("p1", solve(1, 1, O, D))
print("p2", solve(10, 811589153, O, D))