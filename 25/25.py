#!/usr/bin/env python3
file1 = '25.in'

V = []
input = [x.strip() for x in open(file1, 'r').readlines()]
ans = 0
for v in input:
    base = 1
    q = 0
    for x in range(len(v)-1,0-1,-1):
        if v[x]=='-':
            q += -1 * base
        elif v[x] == '=':
            q += -2 * base
        else:
            q += int(v[x]) * base
        base *=5
    ans += q
print(ans)
v = ans
remainder = 0
ans1 = ""

while v > 0:
    remainder = v % 5
    v = v // 5
    print(remainder, v)
    ans1 = str(remainder) + ans1

if v%5 > 0:
    ans1 = str(v%5) + ans1

extra = 0
print("a",ans1)
result = ""
for x in range(len(ans1) - 1, 0-1, -1):
    v = int(ans1[x]) + extra
    extra = 0
    if v > 4:
        extra +=1
        result = '0' + result
    elif v == 4:
        extra += 1
        result = '-' + result
    elif v == 3:
        extra += 1
        result = '=' + result
    else:
        result = str(v) + result
if extra > 0:
    result = str(extra) + result
print(result)
assert(False)
# components = [0] + components + [remainder]
# print(components)
remainder = 0
ans1 = ''
for x in range(len(components)-1, 0, -1):
    if components[x] - 5 > 0:
        components[x-1] += 1
        components[x] -= 5
    if components[x] == 4:
        ans1 += '-'
        components[x-1] += 1
    elif components[x] == 3:
        ans1 += '='
        components[x-1] +=1
    else:
        ans1 += str(components[x])
if components[0] > 0:
    ans1 += str(components[0])
print("ans1",ans1[::-1])
    # ans1+= str(v)
# components.append(remainder)
# # ans1+= str(remainder)
# for i, x in enumerate(reversed(components)):
#     if x == 3:

# print(ans1)