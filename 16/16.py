#!/usr/bin/env python3
# file1 = '16.test'
file1 = '16.in'
from collections import deque
from itertools import permutations
V = {}
F = {}
input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    words = v.split()
    valve = words[1]
    flow = words[4][5:-1]
    t = [x[0:2] for x in words[9:]]
    V[valve] = t
    F[valve] = int(flow)

print(V, F)
r = 0


valves_with_value = ([x for x in F if F[x] > 0])

def shortest_path(a, b, V):
    shortest_length = 100
    visited = {}
    S = deque([(a, a, 0)])
    while len(S) > 0:
        (start, end_, steps) = S.pop()
        for n in V[end_]:
            if (a, n) not in visited or visited[(a, n)] > steps:
                visited[(a, n)] = steps + 1
                S.append((a, n, steps + 1))
    return visited[(a, b)]

distances = {}
for v1 in ['AA'] + valves_with_value:
    for v2 in valves_with_value:
        distances[(v1, v2)] = shortest_path(v1, v2, V)
# print(distances)
# shortest_path('AA', "HH", V)
# print(valves_with_value)
# max_released = 0

# DP = {}

# def find_best_path(a, valves, time_left):
#     max_released = 0
#     if (a, tuple(valves), time_left) in DP:
#         # print('.', end='')
#         return DP[(a, tuple(valves), time_left)]
#     for b in valves:
#         # print(a, b, len(valves))
#         d = distances[(a, b)]
#         flow_time = time_left - d - 1
#         remaining_valves = [x for x in valves if x != b]
#         released = (flow_time * F[b]) + find_best_path(b, remaining_valves, time_left - d - 1)
#         max_released = max(released, max_released)
#     DP[(a, tuple(valves), time_left)] = max_released
#     return max_released

# print(find_best_path('AA', valves_with_value, 30))
# assert(False)
DP2 = {}
def find_best_path_2(a, valves, time_left, players):
    # if len(DP2) % 100000 == 0:
    #     print(len(DP2))
    max_released = 0
    # here we assume that one player cannot open all the gates, so after player 1 is finished, player 2 starts. This doesn't work with the test code (because that one opens all the gates already with 1 player)
    if time_left <= 0 and players == 2:
        max_released = find_best_path_2('AA', valves, 26, 1)

    if (a, tuple(valves), time_left, players) in DP2:
        # print('.', end='')
        return DP2[(a, tuple(valves), time_left, players)]
    
    for b in valves:
        # print(a, b, len(valves))
        d = distances[(a, b)]
        released = 0
        remaining_valves = [x for x in valves if x != b]
        if time_left > d:
            flow_time = time_left - d - 1
            released = (flow_time * F[b]) 
        
        
        released = released + find_best_path_2(b, remaining_valves, time_left - d - 1, players)
        max_released = max(released, max_released)
    
    DP2[(a, tuple(valves), time_left, players)] = max_released
    return max_released

print("part1", find_best_path_2('AA', valves_with_value, 30, 1))
print("part2", find_best_path_2('AA', valves_with_value, 26, 2))
# print(find_best_path('AA', valves_with_value[7:], 26))
# print(sum(distances.values()))
# print(distances)