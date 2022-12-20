#!/usr/bin/env python3
file1 = '17.in'
# file1 = '17.test'

input = [x.strip() for x in open(file1, 'r').readlines()]

moves = [x for x in input[0]]

shapes = [
    [(0,0), (1,0), (2,0), (3,0)], 
    [(1, 0), (0,1), (1,1), (2,1), (1,2)],
    [(0,0), (1,0), (2,0), (2,1), (2,2)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (0,1), (1,1)]
    ]

max_rocks = 1000000000000
# max_rocks = 2022
cur_shape = 0
cur_move = 0
top = 0
lr_bounds = (0, 6)
G = set()
[G.add((x, 0)) for x in range(0, 7)]


PATTERNS = {}

def rockprint(number_of_rocks, top, cur_move, cur_shape, G):
    global PATTERNS
    # create a fingerprint of 30 rows
    max_y = max([y for (x, y) in G])
    signature = (cur_move, cur_shape, frozenset([(x, max_y - y) for (x, y) in G if (max_y - y) < 30]))
    if signature in PATTERNS:
        return PATTERNS[(signature)]
    PATTERNS[(signature)] = (number_of_rocks, top)
    return False
        

def detect_collision(shape, G):
    for x,y in shape:
        if (x, y) in G:
            return True
    return False


def get_next_move(shape):
    global cur_move
    mv_char = moves[cur_move]
    move_value = 0
    left_bound, right_bound = lr_bounds
    if mv_char == '>':
        move_value = 1
        for x, _ in shape:
            if x + 1 > right_bound:
                move_value = 0
    else:
        move_value = -1
        for x, _ in shape:
            if x - 1 < left_bound:
                move_value = 0

    moved_shape = []
    for x, y in shape:
        moved_shape.append((x + move_value, y))

    cur_move += 1
    if cur_move >= len(moves):
        cur_move = 0
    # print(move_value)
    return moved_shape


def get_next_shape():
    global cur_shape
    # set start pos
    start_y = top + 4
    start_x = 2
    next_shape = []
    for x, y in shapes[cur_shape]:
        next_shape.append((x + start_x, y + start_y))
    
    # preselect next shape
    cur_shape += 1
    if cur_shape > 4:
        cur_shape = 0
    
    return next_shape

# print(G)
rocks = 0
p1 = 0
ROCKPRINTS = {}
added_to_top = 0
while rocks < max_rocks:
    shape = get_next_shape()
    # print(shape, top)
    finished = False
    while not finished:
        new_shape_pos = get_next_move(shape)
        if detect_collision(new_shape_pos, G):
            new_shape_pos = shape
        dropped_shape_pos = []    
        for x, y in new_shape_pos:
            dropped_shape_pos.append((x, y - 1))
        if detect_collision(dropped_shape_pos, G):
            dropped_shape_pos = new_shape_pos
            finished = True
        shape = dropped_shape_pos

    # shape is landed
    # print("landed", shape)
    for x, y in shape:
        G.add((x, y))
    top = max([top]+[y for _, y in shape])
    # print(rocks)
    if rocks == 2022:
        p1 = top
    if rocks > 2022 and rockprint(rocks, top, cur_move, cur_shape, G):
            (nnrocks, nntop) = rockprint(rocks, top, cur_move, cur_shape, G)
            dtop = top - nntop
            drocks = rocks - nnrocks
            number_of_iterations = (max_rocks - rocks) // drocks
            rocks += (drocks * number_of_iterations)
            added_to_top += dtop * number_of_iterations
                        
    rocks += 1
        

# print(rocks)
print("part 1", p1)
print("part 2", top + added_to_top)            

    


    
