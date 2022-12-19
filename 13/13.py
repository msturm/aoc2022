#!/usr/bin/env python3
file1 = '13.in'
P = []
input = [x.strip() for x in open(file1, 'r').readlines()]
i = 0
while i < len(input):
    v1 = input[i]
    i += 1
    v2 = input[i]
    i += 1
    P.append([v1, v2])
    i+= 1

def parse_list(l):
    R = []
    x = 0 
    buf = ''
    result = ''
    while x < len(l):
        if l[x] == '[':
            R.append([])
        elif l[x] == ']':
            v = R.pop()
            if len(buf) > 0:
                v.append(int(buf))
                buf = ''

            if len(R) > 0:
                R[-1].append(v)
            else:
                result = v
            
        elif l[x] == ',':
            if len(buf) > 0:
                R[-1].append(int(buf))
                buf = ''
        else:
            buf += l[x]

        # print(l[x], buf, R)
        x += 1
    return v
    
# print(parse_list(P[0][0]))
# print(P[0][0])
# print([parse_list(x[0]) for x in P])
problems = 0

def compare_list(p1, p2):
    # print("compare", p1, p2)
    x = 0
    r = 0
    while x < len(p1):
        if x+1 > len(p2):
            return -1
        
        r = compare_elem(p1[x], p2[x])
        if r != 0:
            return r
        else:
            x += 1
    if r == 0 and len(p2) < len(p1):
        return -1
    elif r == 0 and len(p1) < len(p2):
        return 1
    return r

            

def compare_elem(p1, p2):
    # print("compare", p1, p2)
    if type(p1) is list and type(p2) is list:
        if len(p1) > 0 and len(p2) == 0:
            return -1
        elif len(p1) == 0 and len(p2) > 0:
            return 1
        elif len(p1) == 0 and len(p2) == 0:
            return 0
        else:
            return compare_list(p1, p2)
    elif type(p1) is int and type(p2) is list:
        return compare_list([p1], p2)
    elif type(p1) is list and type(p2) is int:
        return compare_list(p1, [p2])
    elif type(p1) is int and type(p2) is int and p1 < p2:
        return 1
    elif type(p1) is int and type(p2) is int and p1 > p2:
        return -1
    elif type(p1) is int and type(p2) is int and p1 == p2:
        return 0
    else:
        return 0
    


# print(compare_list([1, 1,3, 1, 1], [1, 1, 5, 1, 1]))
# print(compare_list([[1],[2,3,4]], [[1],4]))
# print(compare_list([9], [[8,7,6]]))
# print(compare_list([[4, 4], 4, 4], [[4, 4], 4, 4, 4]))
# print(compare_list([7, 7, 7, 7], [7, 7, 7]))
# print(compare_list([], [3]))
# print(compare_list([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]))
x = 0
ans1 = 0
for x in range(len(P)):
    p1 = parse_list(P[x][0])
    p2 = parse_list(P[x][1])
    if compare_list(p1, p2) == 1:
        ans1 += x + 1

print("p1", ans1)

# part 2
A = []
for p1, p2 in P:
    A.append(parse_list(p1))
    A.append(parse_list(p2))
A.append([[2]])
A.append([[6]])

# print(A)
swap = True
while swap:
    swap = False
    for x in range(len(A)-1):
        p1 = A[x]
        p2 = A[x+1]
        if compare_list(p1, p2) == -1:
            A[x] = p2
            A[x+1] = p1
            swap = True

# [print(x) for x in A]

print("p2", [x+1 for x, y in enumerate(A) if y == [[2]]][0] * [x+1 for x, y in enumerate(A) if y == [[6]]][0])