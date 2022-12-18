#!/usr/bin/env python3
file1 = '12.in'
from collections import deque
input = [x.strip() for x in open(file1, 'r').readlines()]
G = {}
start = (0,0)
end = (0,0)
max_r = len(input)
max_c = len(input[0])

for r in range(len(input)):
    for c in range(len(input[r])):
        if input[r][c] == 'S':
            start = (r, c)
            G[(r,c)] = ord('a') - 97
        elif input[r][c] == 'E':
            end = (r, c)
            G[(r,c)] = ord('z') - 97
        else:
            G[(r, c)] = ord(input[r][c]) - 97

not_found = 0

def find_path(sr, sc):
    global not_found
    # print(sr, sc)
    D = {(0, 1), (1, 0), (-1, 0), (0, -1)}
    todo = deque()
    todo.append((sr, sc, 0))
    S = {(0, 0): 0}
    
    while len(todo) > 0:
        r, c, d = todo.popleft()
        for dr, dc in D:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < max_r and 0 <= cc < max_c and ((G[(rr, cc)] <= G[(r, c)] + 1)):
                # print("here")
                if (rr, cc) not in S:
                    # print("not in S", cd_point, S)
                    S[(rr, cc)] = d + 1
                    todo.append((rr, cc, d + 1))
    if end not in S:
        not_found += 1
        return 9999
    return S[end]

print("part 1", find_path(start[0], start[1]))
print("part 2", min([x for x in [find_path(sr, sc) for sr, sc in G if G[(sr, sc)] == ord('a') - 97]]))