#!/usr/bin/env python3
file1 = '19.in'
# file1 = '19.test'
from collections import defaultdict
from collections import deque

# Blueprint 14: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 15 obsidian.



# robots: 0 geode, 1 obs, 2 clay, 3 ore
def collect_resources(robots, resources):
    return (robots[3] + resources[0],
            robots[2] + resources[1],
            robots[1] + resources[2],
            robots[0] + resources[3],
        )

def build_robots(blue_print, resources, robots):
    for i, costs in enumerate(blue_print):
        (orec, clayc, obsc) = costs
        # print("costs", orec, clayc, obsc)
        (orer, clayr, obsr, geodr) = resources
        # print("resources", orer, clayr, obsr, geodr)
        if orer >= orec and clayr >= clayc and obsr >= obsc: # build robot
            robots[i] += 1
            orer -= orec
            clayr -= clayc
            obsr -= obsc
            resources = (orer, clayr, obsr, geodr)
    return (resources, robots)

def simulate_robot(id, blue_print, t):
    # state (ore, clay, obsidian, geode, robot1, robot2, robot3, robot4, time)
    (ore_robot_costs, clay_robot_costs, obsidian_robot_costs, geode_robot_costs) = blue_print
    S = (0,0,0,0,1,0,0,0,t)

    SEEN = set()
    Q = deque([S])
    best = 0 #number of geode

    while Q:
        state = Q.pop()
        (ore, clay, obsidian, geode, r1, r2, r3, r4, t) = state
        if t == 0:
            best = max(best, geode)
            continue

        # throw away resources we're not going to need anyway
        # max possible robots to build: t * (cost or resource of most expensive robot)

        
        max_ore_needed = t * max(ore_robot_costs, clay_robot_costs, obsidian_robot_costs[0], geode_robot_costs[0])
        max_clay_needed = t * obsidian_robot_costs[1]
        max_obsidian_needed = t * geode_robot_costs[1]
        if ore >= max_ore_needed:
            ore = max_ore_needed
        if clay >= max_clay_needed:
            clay = max_clay_needed
        if obsidian >= max_obsidian_needed:
            obsidian = max_obsidian_needed
        
        max_ore_per_turn = max(ore_robot_costs, clay_robot_costs, obsidian_robot_costs[0], geode_robot_costs[0])
        if r1 >= max_ore_per_turn: 
            r1 = max_ore_per_turn
        if r2 >= obsidian_robot_costs[1]:
            r2 = obsidian_robot_costs[1]
        if r3 >= geode_robot_costs[1]:
            r3 = geode_robot_costs[1]
        
        state = (ore, clay, obsidian, geode, r1, r2, r3, r4, t) 

        if state in SEEN:
            continue
        SEEN.add(state)

        # debug
        if len(SEEN) % 1000000 == 0:
            print(len(SEEN), best, t)

        # build no new robot:
        Q.append((ore + r1, clay + r2, obsidian + r3, geode + r4, r1, r2, r3, r4, t-1))

        # build a robot
        if ore >= ore_robot_costs:
            Q.append((ore + r1 - ore_robot_costs, clay + r2, obsidian + r3, geode + r4, r1 + 1, r2, r3, r4, t-1))
        if ore >= clay_robot_costs:
            Q.append((ore + r1 - clay_robot_costs, clay + r2, obsidian + r3, geode + r4, r1, r2+1, r3, r4, t-1))
        if ore >= obsidian_robot_costs[0] and clay >= obsidian_robot_costs[1]:
            Q.append((ore + r1 - obsidian_robot_costs[0], clay + r2 - obsidian_robot_costs[1], obsidian + r3, geode + r4, r1, r2, r3+1, r4, t-1))
        if ore >= geode_robot_costs[0] and obsidian >= geode_robot_costs[1]:
            Q.append((ore + r1 - geode_robot_costs[0], clay + r2 , obsidian + r3 - geode_robot_costs[1], geode + r4, r1, r2, r3, r4+1, t-1))
    print(len(SEEN), best)
    return best



input = [x.strip() for x in open(file1, 'r').readlines()]
Blueprints = {}
for v in input:
    words = v.split()
    blueprint_id = int(words[1][:-1])
    # costs (ore, clay, obsidian)
    ore_robot_costs = int(words[6])
    clay_robot_costs = int(words[12])
    obsidian_robot_costs = (int(words[18]), int(words[21]))
    geode_robot_costs = (int(words[27]),int(words[30]))
    Blueprints[blueprint_id] = (ore_robot_costs, clay_robot_costs, obsidian_robot_costs, geode_robot_costs)

p1 = 0
for x in Blueprints:
    p1 += x*simulate_robot(x, Blueprints[x], 24)
print("p1", p1)
p2 = 1
# print(simulate_robot(1, Blueprints[1], 32))
for x in list(Blueprints.keys())[0:3]:
    p2 *= simulate_robot(x, Blueprints[x], 32)

print("p2", p2)