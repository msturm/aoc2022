#!/usr/bin/env python3
import re
file1 = '22.in'
# file1 = '22.test'

input = [x for x in open(file1, 'r').readlines()]

G = {}
moves = []

number_of_rows = 0
number_of_columns = 0
for r, v in enumerate(input):
    number_of_columns = max(number_of_columns, len(v))
    if len(v.strip()) > 0:
        for c, v1 in enumerate(v):
            if v1 == '.':
                G[r, c] = '.'
            elif v1 == '#':
                G[r, c] = '#'
    else:
        number_of_rows = r
        break

moves = input[-1].strip()
# moves = "10R5L5R10L4R5L"
move_pointer = 0
# print(moves)

r_bounds = {} # holds start and end of rows
c_bounds = {} # holds start and end of rows
side_length = 0

## calculate bounds
for r in range(0, number_of_rows):
    west_bound = number_of_columns + 1
    east_bound = 0
    for c in range(0, number_of_columns):
        if (r, c) in G:
            west_bound = min(west_bound, c)
            east_bound = max(east_bound, c)
    r_bounds[r] = (west_bound, east_bound)

for c in range(0, number_of_columns):
    north_bound = number_of_rows + 1
    south_bound = 0
    for r in range(0, number_of_rows):
        if (r, c) in G:
            north_bound = min(north_bound, r)
            south_bound = max(south_bound, r)
    c_bounds[c] = (north_bound, south_bound)

side_length = min([r_bounds[x][1]-r_bounds[x][0] for x in range(0, number_of_rows)])

# print(G)
def change_dir(dir, v):
    new_dir = dir
    if v == 'L':
        new_dir = (dir - 1) % 4
    else:
        new_dir = (dir + 1) % 4
    print("change_dir", dir, new_dir, v)
    return new_dir

# (r, c) -> (side, r in side, c in side)
pos_to_side = {}
# (side, r in side, c in side) -> (r, c)
side_to_pos = {}

def identify_sides():
    global pos_to_side, side_to_pos
    S = {}
    N = {}
    r = 0
    square_count = 0
    # print(side_length)
    square_location = (0, 0) 
    # print(number_of_columns, number_of_rows)
    side_id = 0
    for r in range(0, number_of_rows -1, side_length+1):
        for c in range(0, number_of_columns-1, side_length+1):
            square_location = (r // (side_length+1), c//(side_length+1))
            # print(square_location)
            if (r, c) in G:
                new_square = {}
                for rr in range(0, side_length+1):
                    for cc in range(0, side_length+1):
                        new_square[(r+rr, c+cc)] = (rr, cc)
                        pos_to_side[(r+rr,c+cc)] = (side_id, rr, cc)
                        side_to_pos[(side_id, rr, cc)] = (r+rr, c+cc)
                S[side_id] = new_square
                side_id += 1
                
    print(len(S))
    return S

def print_square(s):
    for r in range(0,side_length+1):
        for c in range(0, side_length+1):
            print(s[(r, c)], end="")
        print("")
    print("")


# real

def rotate_and_move(r, c, dir, nr_of_rotations = 1):
    new_r, new_c, new_dir = r, c, dir
    for _ in range(nr_of_rotations):
        new_r, new_c, new_dir = (new_c, side_length-new_r, (new_dir +1)%4)
    print(new_r, new_c)
    if new_dir == 0:
        new_c = (new_c)%side_length
    elif new_dir == 1:
        new_r = (new_r)%side_length
    elif new_dir == 2:
        new_c = side_length
    elif new_dir == 3:
        new_r = side_length
    return (new_r, new_c, new_dir)

    
#rotate and move
def perform_move(cur_pos, dir):
    global pos_to_side, side_to_pos, sides_mapping
    side_id, side_r, side_c = pos_to_side[cur_pos]
    side = sides[side_id]

    new_dir = dir
    (new_r, new_c) = cur_pos
    if dir == 0:
        new_c += 1
        if (new_r, new_c) not in side:
            (new_side, rotations) = sides_mapping[side_id][0]
            (side_r, side_c, new_dir) = rotate_and_move(side_r, side_c, new_dir, rotations)
            (new_r, new_c) = side_to_pos[(new_side, side_r, side_c)]
    elif dir == 1:
        new_r += 1
        if (new_r, new_c) not in side:
            (new_side, rotations) = sides_mapping[side_id][1]
            (side_r, side_c, new_dir) = rotate_and_move(side_r, side_c, new_dir, rotations)
            (new_r, new_c) = side_to_pos[(new_side, side_r, side_c)]   
    elif dir == 2:
        new_c -= 1
        if (new_r, new_c) not in side:
            (new_side, rotations) = sides_mapping[side_id][2]
            (side_r, side_c, new_dir) = rotate_and_move(side_r, side_c, new_dir, rotations)
            (new_r, new_c) = side_to_pos[(new_side, side_r, side_c)]    
    elif dir == 3:
        new_r -= 1
        if (new_r, new_c) not in side:
            (new_side, rotations) = sides_mapping[side_id][3]
            (side_r, side_c, new_dir) = rotate_and_move(side_r, side_c, new_dir, rotations)
            (new_r, new_c) = side_to_pos[(new_side, side_r, side_c)] 
    if G[(new_r, new_c)] == '#':
        (new_r, new_c) = cur_pos
        new_dir = dir
    return ((new_r, new_c), new_dir)


sides = identify_sides()
# print([s for s in sides])
# [print_square(sides[s]) for s in sides]
# print([(x, sides[x][1]) for x in sides])

# sides mapping: side_id: [(right neighbour_id, rotations), (bottom neighbour_id, rotations), (left neighbour_id, rotations), (top neighbour_id, rotations)]
# test
# sides_mapping = {0: [(5,2),(3,0),(2,3),(4,0)], 1: [(2,0),(4,3),(5,1),(0,2)], 2: [(3,0),(4,3),(1,0),(0,1)], 3:[(5,1),(4,0),(2,0),(0,0)], 4:[(5,0),(1,2),(2,1),(3,0)], 5: [(0,3),(1,3),(4,0),(3,3)]}
sides_mapping = {0: [(1,0),(2,0),(3,2),(5,1)], 1: [(4,2),(2,1),(0,0),(5,0)], 2: [(1,3),(4,0),(3,3),(0,0)], 3: [(4,0),(5,0),(0,2),(2,1)], 4: [(1,2),(5,1),(3,0),(2,0)], 5: [(4,3),(1,0),(0,3),(3,0)]}
# sides_mapping = {0: [(5,2),(3,0),(2,3),(4,0)], 1: [(2,0),(4,3),(5,1),(0,2)]}
# print("5,11 -> 8,14 1", perform_move((5,11), 0))
# print("1,11 -> 10,15 2", perform_move((1,11), 0))
# print("11,10 -> 7,1 3", perform_move((11,10), 1))
# print("4,6 -> 2,8 0", perform_move((4,6), 3))
# assert(False)

def get_next_move():
    global moves, move_pointer
    if move_pointer < len(moves):
        if moves[move_pointer] == 'L':
            move_pointer += 1
            return 'L'
        elif moves[move_pointer] == 'R':
            move_pointer += 1
            return 'R'
        else:
            steps = moves[move_pointer]
            if move_pointer + 1 < len(moves) and moves[move_pointer+1] != 'L' and moves[move_pointer+1] != 'R':
                steps += moves[move_pointer+1]
                move_pointer += 1
            move_pointer +=1
            return int(steps)
    else:
        return ''
        
path = {}

def dir_to_arrow(dir):
    if dir == 0:
        return '>'
    if dir == 1:
        return 'V'
    if dir == 2:
        return '<'
    if dir == 3:
        return '^'

def solve():
    global path
    dir = 0 # 0: East, 1: South, 2: West, 3: North
    cur_pos = (0, r_bounds[0][0])
    path[cur_pos] = dir_to_arrow(dir)
    next_move = get_next_move()
    while next_move != '':
        print("move", next_move, cur_pos, dir)
        if next_move == 'L' or next_move == 'R':
            dir = change_dir(dir, next_move)
            path[cur_pos] = dir_to_arrow(dir)
        else:
            for x in range(0, next_move):
                cur_pos, dir = perform_move(cur_pos, dir)
                path[cur_pos] = dir_to_arrow(dir)
        
        next_move = get_next_move()
    print(cur_pos[0], cur_pos[1], dir)    
    return 1000 * (cur_pos[0]+1) + 4 * (cur_pos[1]+1) + dir

def print_grid():
    global number_of_columns, number_of_rows, path, G
    for r in range(0, number_of_rows):
        for c in range(0, number_of_columns):
            char = ' '
            if (r, c) in G:
                char = G[(r,c)]
            if (r, c) in path:
                char = path[(r, c)]
            print(char, end="")
        print("")


print(solve())
print_grid()
print(moves)
# print(path)
        
