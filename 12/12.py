#!/usr/bin/env python3
file1 = '12.test'
G = {}
start = (0,0)
end = (0,0)

input = [x.strip() for x in open(file1, 'r').readlines()]
for r in range(len(input)):
    for c in range(len(input[r])):
        if input[r][c] == 'S':
            start = (r, c)
            G[(r,c)] = 0
        elif input[r][c] == 'E':
            end = (r, c)
            G[(r,c)] = 26
        else:
            G[(r, c)] = ord(input[r][c]) - 97
path = [start]
D = {(0, 1), (1, 0), (-1, 0), (0, -1)}
while path[-1] != end:
    cur = path[-1]
    if cur[0] < end[0] and G[(cur[0]+1,cur[1])] <= (G[(cur[0],cur[1])] + 1) and (cur[0]+1,cur[1]) not in path:
        path.append((cur[0] + 1, cur[1]))
    elif cur[1] < end[1] and G[(cur[0],cur[1]+1)] <= (G[(cur[0],cur[1])] + 1) and (cur[0],cur[1]+1) not in path:
        path.append((cur[0], cur[1] + 1))
    elif cur[0] > end[0] and G[(cur[0] - 1,cur[1])] <= (G[(cur[0],cur[1])] + 1) and (cur[0] - 1,cur[1]) not in path:
        path.append((cur[0] - 1, cur[1]))
    elif cur[1] > end[1] and G[(cur[0],cur[1]-1)] <= (G[(cur[0],cur[1])] + 1) and (cur[0],cur[1]-1) not in path:
        path.append((cur[0], cur[1] - 1)) 
    elif cur[0] >= end[0] and G[(cur[0]+1,cur[1])] <= (G[(cur[0],cur[1])] + 1) and (cur[0]+1,cur[1]) not in path:
        path.append((cur[0] + 1, cur[1]))
    elif cur[1] >= end[1] and G[(cur[0],cur[1]+1)] <= (G[(cur[0],cur[1])] + 1) and (cur[0],cur[1]+1) not in path:
        path.append((cur[0], cur[1] + 1))
    elif cur[0] >= end[0] and G[(cur[0] - 1,cur[1])] <= (G[(cur[0],cur[1])] + 1) and (cur[0] - 1,cur[1]) not in path:
        path.append((cur[0] - 1, cur[1]))
    elif cur[1] >= end[1] and G[(cur[0],cur[1]-1)] <= (G[(cur[0],cur[1])] + 1) and (cur[0],cur[1]-1) not in path:
        path.append((cur[0], cur[1] - 1)) 
    print(path)
print(start, end, G)