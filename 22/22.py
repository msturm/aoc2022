#!/usr/bin/env python3
import re
file1 = '22.in'
# file1 = '22.test'

input = [x for x in open(file1, 'r').readlines()]

G = {}
moves = []

number_of_rows = 0
number_of_columns = len(input[0])
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
print(number_of_columns)
assert(False)
moves = input[-1].strip()
move_pointer = 0
# print(moves)


r_bounds = {} # holds start and end of rows
c_bounds = {} # holds start and end of rows

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

# print(G)
def change_dir(dir, v):
    new_dir = dir
    if v == 'L':
        new_dir = (dir - 1) % 4
    else:
        new_dir = (dir + 1) % 4
    print("change_dir", dir, new_dir, v)
    return new_dir

def perform_move(cur_pos, dir):
    # for s in range(0, steps):
    (new_r, new_c) = cur_pos
    # print(cur_pos, dir)
    if dir == 0:
        new_c += 1
        if (new_r, new_c) not in G:
            new_c = r_bounds[new_r][0]    
    elif dir == 1:
        new_r += 1
        if (new_r, new_c) not in G:
            new_r = c_bounds[new_c][0]    
    elif dir == 2:
        new_c -= 1
        if (new_r, new_c) not in G:
            new_c = r_bounds[new_r][1]    
    elif dir == 3:
        new_r -= 1
        if (new_r, new_c) not in G:
            new_r = c_bounds[new_c][1]
    if G[(new_r, new_c)] == '#':
        (new_r, new_c) = cur_pos
    # print(new_r, new_c, dir)
    return (new_r, new_c)

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
                cur_pos = perform_move(cur_pos, dir)
                path[cur_pos] = dir_to_arrow(dir)
        
        next_move = get_next_move()
        
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
# print_grid()
# print(path)
        
