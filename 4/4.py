#!/usr/bin/env python3
file1 = '4.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
count1 = 0
count2 = 0
for v in input:
    s1, s2 = [x.split('-') for x in v.split(',')]
    s1 = [int(y) for y in s1]
    s2 = [int(y) for y in s2]

    if (s1[0] <= s2[0] and s1[1] >= s2[1]):
        count1 += 1
        count2 += 1
    elif (s2[0] <= s1[0] and s2[1] >= s1[1]):
        count1 += 1
        count2 += 1
    elif (s1[0] <= s2[0] and s1[1] >= s2[0]):
        count2 += 1
    elif (s2[0] <= s1[0] and s2[1] >= s1[0]):
        count2 += 1
    elif (s1[0] <= s2[1] and s1[1] >= s2[1]):
        count2 += 1
    elif (s2[0] <= s1[1] and s2[1] >= s1[1]):
        count2 += 1

print(count1)
print(count2)