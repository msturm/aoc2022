#!/usr/bin/env python3
file1 = '23.in'
# file1 = '23.test'

E = set()

input = [x.strip() for x in open(file1, 'r').readlines()]
for r, v in enumerate(input):
    for c, e in enumerate(v):
        if e=='#':
            E.add((r, c))

moves_condition = [[(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)],[(-1,-1),(0,-1),(1,-1)],[(-1,1),(0,1),(1,1)]]
move = [(-1,0),(1,0),(0,-1),(0,1)]
preferred_move = 0

# print( [(rr,cc) for mc in moves_condition for move in mc])
# assert(False)

def get_proposed_loc():
    global E, moves_condition
    proposal = {}
    # print("elfs", len(E))
    for (r, c) in E:
        found_new_location = False
        m = 0
        
        fields_around_elf = [(rr,cc) for mc in moves_condition for (rr,cc) in mc]
        if all([(r+rr, c+cc) not in E for (rr,cc) in fields_around_elf]):
            # print((r, c), "->", (r, c), "(no elves around)")
            proposal[(r, c)] = (r,c)
        else:
            while m < 4 and not found_new_location:
                pm = (m + preferred_move) % 4
                if all([(r+rr, c+cc) not in E for (rr, cc) in moves_condition[pm]]):
                    rr, cc = move[pm]
                    if (r+rr, c+cc) not in proposal:
                        # print((r, c), "->", (r+rr, c+cc), pm,m)
                        proposal[(r+rr, c+cc)] = (r,c)
                    else:
                        reverted_elf = proposal.pop((r+rr, c+cc))
                        proposal[(r+rr, c+cc)] = 'X'
                        if reverted_elf != 'X':
                            proposal[reverted_elf] =  reverted_elf
                        proposal[(r, c)] = (r,c)
                    found_new_location = True
                m += 1
            if not found_new_location:
                # print((r, c), "->", (r, c), pm,m)
                proposal[(r, c)] = (r,c)
        

    
    new_elves = set()

    for (r, c) in proposal:
        if not proposal[(r, c)] == 'X':
            new_elves.add((r, c))
    # print(new_elves)
    return new_elves


def print_grid(elves):
    min_r = min([r for (r, _) in elves]) - 2
    max_r = max([r for (r, _) in elves]) + 3
    min_c = min([c for (_, c) in elves]) - 2
    max_c = max([c for (_, c) in elves]) + 3

    for r in range(0, max_r):
        for c in range(0, max_c):
            if (r, c) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print("")


def find_empty_fields(elves):
    count = 0
    min_r = min([r for (r, _) in elves])
    max_r = max([r for (r, _) in elves])+1
    min_c = min([c for (_, c) in elves])
    max_c = max([c for (_, c) in elves])+1
    # print(min_r, max_r, min_c, max_c)
    for r in range(min_r, max_r):
        for c in range(min_c, max_c):
            if (r, c) not in elves:
                count += 1
    return count

# print_grid(E)
count = 0
elves_moved = True
p1 = 0
p2 = 0
while elves_moved :
    count +=1 
    print("round", count)
    if count == 11:
        p1 = find_empty_fields(E)
    new_E = get_proposed_loc()
    # print("compare", new_E == E)
    if new_E == E:
        elves_moved = False
        p2 = count
    
    E = new_E
    # print_grid(E)
    preferred_move +=1
print_grid(E)
print("p1", p1)
print("p2", p2)
