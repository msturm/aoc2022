#!/usr/bin/env python3
file1 = '10.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
stack = []
sprite = [0, 1, 2]
cycle = 1
line = 0
ptr = 0
wait = 0
x = 1
ans = 0
cycles = [20, 60, 100, 140, 180, 220]
scr_line = ""
pxl = 0
while cycle < 241:
    print(cycle, pxl, sprite, len(scr_line))
    pxl = (cycle - 1) % 40
    if cycle in cycles:
        # print("cycle", cycle, x, cycle*x)
        ans += cycle * x
    # print(cycle, x, wait, ans, ptr, input[ptr])
    
    if pxl in sprite:
        scr_line += "#"
    else:
        scr_line += "."
    
    if len(stack) > 0:
        x += stack.pop()
        sprite = [x-1, x, x+1]
    else:
        words = input[ptr].split()
        if len(words) == 1: # noop
            ptr += 1
        elif len(words) == 2: # addx
            stack.append(int(words[1]))
            ptr += 1
    # print(cycle, x, wait)
    cycle += 1

print(ans)
for x in range(0, 240, 40):
    print(scr_line[x: x+40])
