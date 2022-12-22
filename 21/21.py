#!/usr/bin/env python3
file1 = '21.in'
# file1 = '21.test'

M = {}
S = {}
input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    words = v.split()
    monkey_name = words[0][:-1]
    monkey_data = words[1:]
    M[monkey_name] = monkey_data

# print(len(M))
num_monkeys = len(M)
c = 0
# while len(S) < num_monkeys:
#     for m, v in M.items():
#         c += 1
#         if len(v) == 1: # number
#             S[m] = int(v[0])
#         else:
#             (m1, op, m2) = v
#             if m1 in S and m2 in S:
#                 res = 0
#                 v1, v2 = S[m1],S[m2]
#                 if op == '+':
#                     res = v1 + v2
#                 elif op == '-':
#                     res = v1 - v2
#                 elif op == '/':
#                     res = v1//v2
#                 else:
#                     res = v1 * v2
#                 S[m] = res
#         if c % 1000 == 0:
#             print(c)
#     for k in S:
#         if k in M:
#             M.pop(k)



def solve(human, M, prev):
    S = {}
    global c
    while len(S) < num_monkeys:
        for m, v in M.items():
            c += 1
            if len(v) == 1: # number
                S[m] = int(v[0])
                S['humn'] = human
            else:
                (m1, op, m2) = v
                if m1 in S and m2 in S:
                    res = 0
                    v1, v2 = S[m1],S[m2]
                    if m == 'root':
                        print(human, S[m1], S[m2], S[m1]-S[m2])
                        if prev > 0 and (S[m1]-S[m2]) < 0:
                            print(human)
                            assert(False)
                        if S[m1]-S[m2] == 0:
                            print(human)
                            assert(False)
                        return S[m1]-S[m2]
                    elif op == '+':
                        res = v1 + v2
                    elif op == '-':
                        res = v1 - v2
                    elif op == '/':
                        res = v1//v2
                    else:
                        res = v1 * v2
                    S[m] = res
            # if c % 1000 == 0:
                # print(c)
        for k in S:
            if k in M:
                M.pop(k)    
    # break
    
    # print(S, len(S), len(M))
prev = solve(1, M.copy(), 1000)
for i in range(3558714869400,3558714869500,1):
    prev = solve(i, M.copy(), prev)
print(S['root'])
