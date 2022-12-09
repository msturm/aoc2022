#!/usr/bin/env python3
file1 = '9.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
part1 = set()
part2 = set()
knots = [(0,0)] * 10 #tuple: (row, column)
part1.add(tuple(knots[0]))
D = { (2, 0): (1, 0), (-2, 0): (-1, 0), (0, 2): (0, 1), (0, -2): (0, -1), (2, 1): (1, 1), (1, 2): (1, 1), (-1, -2): (-1, -1), (-2, -1): (-1, -1), (-2, 1): (-1, 1), (2, -1):(1, -1), (-1, 2): (-1, 1), (1, -2): (1, -1),
 (2, 2): (1, 1), (2, -2): (1, -1), (-2, -2): (-1, -1), (-2, 2): (-1, 1) }
for v in input:
    dir, amount = v.split()
    amount = int(amount)
    for x in range(0, amount):
        head_knot = knots[0]
        if dir == 'L':
            head_knot = (head_knot[0], head_knot[1] - 1)
        elif dir == 'R':
            head_knot = (head_knot[0], head_knot[1] + 1)
        elif dir == 'U':
            head_knot = (head_knot[0] - 1, head_knot[1])
        elif dir == 'D':
            head_knot = (head_knot[0] + 1, head_knot[1])
        knots[0] = head_knot

        for n in range(len(knots)):
            if n > 0:
                knot = knots[n]
                prev_knot = knots[n - 1]
                shift = (prev_knot[0] - knot[0], prev_knot[1] - knot[1])
                if shift in D:
                    knots[n] = (knot[0] + D[shift][0], knot[1] + D[shift][1])
        print(knots)
        part2.add(knots[-1])
        # print(shift, t_pos, h_pos)
        part1.add(knots[1])
print(len(part1))
print(len(part2))
