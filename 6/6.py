#!/usr/bin/env python3
from collections import deque
file1 = '6.in'

input = [x.strip() for x in open(file1, 'r').readlines()][0]
# input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
recent = deque()
recent2 = deque()
ans1 = 0
ans2 = 0
start = 0
n = 0
while n < len(input):
    x = input[n]
    print(n, x)
    if x in recent2:
        start = start + 1
        n = start
        recent2.clear()
    else:
        n += 1
        recent2.append(x)

    if len(recent2) == 4 and ans1 == 0:
        ans1 = n
        break

start = 0
n = 0
while n < len(input):
    x = input[n]
    if x in recent2:
        start = start + 1
        n = start
        recent2.clear()
    else:
        n += 1
        recent2.append(x)

    if len(recent2) == 14 and ans2 == 0:
        ans2 = n
        break

print(ans1)
print(ans2)