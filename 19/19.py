#!/usr/bin/env python3
file1 = '19.test'
from collections import defaultdict

# Blueprint 14: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 15 obsidian.

input = [x.strip() for x in open(file1, 'r').readlines()]
Blueprints = {}
for v in input:
    words = v.split()
    blueprint_id = int(words[1][:-1])
    # costs (ore, clay, obsidian)
    ore_cost = (int(words[6]), 0, 0)
    clay_cost = (int(words[12]), 0, 0)
    obsidian_cost = (int(words[18]), int(words[21]), 0)
    geode_cost = (int(words[27]),0,int(words[30]))
    Blueprints[blueprint_id] = list(reversed([ore_cost, clay_cost, obsidian_cost, geode_cost]))


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

def simulate_robot(blue_print):
    robots = {0:0, 1:0, 2:0, 3:1}
    resources = (0, 0, 0, 0)
    time_left = 24
    while time_left > 0:
        resources = collect_resources(robots, resources)
        (resources, robots) = build_robots(blue_print, resources, robots)
        print(resources, robots)
        time_left -= 1
        

simulate_robot(Blueprints[1])

