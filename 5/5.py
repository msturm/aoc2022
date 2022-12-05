#!/usr/bin/env python3
from collections import deque
from copy import deepcopy
file1 = '5.in'
stacks = []
input = [x for x in open(file1, 'r').readlines()]
commands = False
lc = 0
num_stacks = 0
for v in input:
    if len(v.strip()) == 0:
        num_stacks = max([int(x.strip()) for x in input[lc -1].split()])
        for x in range(0, num_stacks):
            stacks.append(deque())
        break
    lc += 1

for x in range(0, lc-1):
    for y in range(0, num_stacks):
        si = 1+(y*4) if y > 0 else 1
        crate = input[x][si:si+1]
        if len(crate.strip()) > 0:
            stacks[y].appendleft(crate)
stacks2 = deepcopy(stacks)
print(stacks)
# Move crates
for v in input[lc+1:]:
    v = v.strip()
    count = int(v.split()[1])
    source = int(v.split()[3])-1
    target = int(v.split()[5])-1
    for x in range(0, count):
        # print(stacks[source], stacks[target])
        value = stacks[source].pop()
        stacks[target].append(value)
        # print(stacks[source], stacks[target])
    
    temp_store = []
    print("before", stacks2[source], stacks2[target], v)
    for x in range(0, count):
        temp_store.append(stacks2[source].pop())
    temp_store.reverse()
    [stacks2[target].append(x) for x in temp_store]
    print("after", stacks2[source], stacks2[target])
        

# print(stacks)
print("part1", "".join([x[-1] for x in stacks]))
# print(stacks2)
print("part2", "".join([x[-1] for x in stacks2]))