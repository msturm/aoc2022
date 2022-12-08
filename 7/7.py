#!/usr/bin/env python3
from collections import deque,defaultdict
file1 = '7.deep'
dirstack = []
dirs = defaultdict(int)
c = 0
# input = [x.strip() for x in open(file1, 'r').readlines()]
for v in open(file1, 'r'):
    words = v.strip().split()
    if c % 100 == 0:
        print(c)
    c += 1
    path = "/".join(dirstack)

    if words[1] == "cd":
        if words[2] == "..":
            dirstack.pop()
            parent = "/".join(dirstack)
            dirs[parent] += dirs[path]
        else:
            dirstack.append(words[2])
    elif words[1] != '$' and words[0] != "dir": # dirlisting
        if words[0].isnumeric():
            dirs[path] += int(words[0])

    parent = "/".join(dirstack[:-1])
    # print(v, dirstack, dirs[parent])

# print(dirstack)
while len(dirstack) > 1:
    path = "/".join(dirstack)
    dirstack.pop()
    parent = "/".join(dirstack)
    dirs[parent] += dirs[path]
    # print(dirs[dirstack[-1]], dirstack)
    
# print([x for x in dirs.items() if x[1] <= 100000])
# print([x for x in dirs.items() if x[1] > 100000])
print("ans1", sum([x[1] for x in dirs.items() if x[1] <= 100000]))
free_space = 70000000 - dirs['/']
needed_space = 30000000 - free_space
print("ans2", min([x[1] for x in dirs.items() if x[1] > needed_space]))
