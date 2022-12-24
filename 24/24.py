#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
import sys 
sys.setrecursionlimit(10000)
file1 = '24.in'
# file1 = '24.test'
G = defaultdict(set)
max_r = 0
max_c = 0
pos = (-1,0)
input = [x.strip() for x in open(file1, 'r').readlines()]
for r, v1 in enumerate(input):
    for c, v2 in enumerate(v1):
        if v2 in ['<','>','v','^']:
            G[(r-1,c-1)].add(v2)
    max_c = c-1
max_r = r -1

print(G, max_r, max_c, pos)

D = {(0,1),(1,0),(0,-1),(-1,0),(0,0)}



def fingerprint_grid(g):
    result = ''
    for k,v in g.items():
        (r,c) = k
        result += str(r) + ',' + str(c) + ':' +str(v)
    # print(result)
    return result

SEEN_GRID = {}
def get_next_grid(g):
    global SEEN_GRID, max_r, max_c
    fpg = fingerprint_grid(g)
    if fpg in SEEN_GRID:
        return SEEN_GRID[fpg]
    new_g = defaultdict(set)
    for k, v1 in g.items():
        for v in v1:
            (r, c) = k
            if v == '>':
                c = c+1 if c<max_c-1 else 0
            elif v == '<':
                c = c-1 if c>0 else max_c - 1
            elif v == 'v':
                r = r+1 if r<max_r-1 else 0
            else:
                r = r-1 if r>0 else max_r - 1
            new_g[r,c].add(v)
    SEEN_GRID[fpg] = new_g
    return new_g

def print_grid(g, pos = (-1,0)):
    
    for r in range(0, max_r):
        for c in range(0, max_c):
            if pos == (r,c):
                print("E", end='')
            elif (r, c) in g:
                if len(g[(r,c)]) > 1:
                    print(len(g[(r,c)]), end='')
                else:
                    print(list(g[(r,c)])[0], end='')
            else:
                print('.', end="")
        print("")
    print("")

# print(solve((-1,0),G,0))


g_state = defaultdict(list)
def solve(start, destination):
    global g_state
    ng = g_state
    S = deque([(start,ng,0)])
    min_moves = int(1e7)
    tried = set()
    (des_r, des_c) = destination
    
    while S:
        pos, g, moves = S.popleft()
        if (pos, moves) in tried:
            continue

        # if destination == (0,0):
            # print(start)
            # print_grid(ng, pos)
            # return None
        
        tried.add((pos, moves))
        (r, c) = pos
        if (r, c) == (des_r,des_c):
            g_state = get_next_grid(g)     
            return moves + 1
        else:
            # print(len(S), (r,c), moves)
            # print_grid(g, pos)
            next_g = get_next_grid(g)
            for (rr, cc) in D:
                (new_r, new_c) = (r+rr,c+cc)
                # print(new_r, new_c, moves,"not added")
                if (0 <= new_r < max_r and 0 <= new_c < max_c and (new_r,new_c) not in next_g and ((new_r, new_c), moves+1) not in tried) or (new_r,new_c)==start:
                    # print(new_r, new_c, moves,"added")
                    # print_grid(next_g,(new_r,new_c))
                    print((new_r, new_c), moves+1)
                    S.append(((new_r, new_c), next_g, moves+1))
                # elif ((r,c),moves+1) not in tried:
                    # S.append(((r, c), next_g, moves+1))

g_state = G
p1 = solve((-1, 0),(max_r-1,max_c-1))
print("p1", p1)
print_grid(g_state)
back = solve((max_r,max_c-1), (0,0))
print(back)
print("p2", p1+back+solve((-1, 0),(max_r-1,max_c-1)))

# for i in range(0,6):
    # print_grid(ng)
    # ng = get_next_grid(ng)