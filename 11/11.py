#!/usr/bin/env python3
file1 = '11.in'
from math import gcd
from functools import reduce

input = [x.strip() for x in open(file1, 'r').readlines()]

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)


def calculate_ans(part2 = False):
    n = 0
    monkeys = []
    while n < len(input):
        if len(input[n].strip()) == 0:
            n += 1
        else:
            curMonkey = int(input[n].split()[1][:-1])
            n += 1
            monkeys.append({"items":[int(x.strip()) for x in input[n].split(":")[1].split(",")]})
            n += 1
            monkeys[curMonkey]["op"] = input[n].split(":")[1].strip().split()[-2:]
            n += 1
            monkeys[curMonkey]["test"] = int(input[n].split(":")[1].strip().split()[-1])
            n += 1
            monkeys[curMonkey]["test_true"] = int(input[n].split(":")[1].split()[-1])
            n += 1
            monkeys[curMonkey]["test_false"] = int(input[n].split(":")[1].split()[-1])
            n += 1
            monkeys[curMonkey]["inspected"] = 0


    monkey_lcm = lcm([x["test"] for x in monkeys])
    rounds = 20 if not part2 else 10000
    for s in range(rounds):
        for monkey in monkeys:
            for x in monkey["items"]:
                monkey["inspected"] += 1
                result = x
                op_val = x if not monkey["op"][1].isnumeric() else int(monkey["op"][1])
                
                if monkey["op"][0] == '+':
                    x += op_val
                else: # *  
                    x *= op_val
                
                if not part2:
                    x = x // 3
                else: 
                    x = x % monkey_lcm
                    
                if x % monkey["test"] == 0:
                    monkeys[monkey["test_true"]]["items"].append(x)
                else:
                    monkeys[monkey["test_false"]]["items"].append(x)
                # print("monkey", [x['items'] for x in monkeys])
            monkey["items"] = []
        #print(s, [x['items'] for x in monkeys])
    res1 = list(reversed(sorted([x['inspected'] for x in monkeys])))
    return res1[0] * res1[1]
print(calculate_ans())
print(calculate_ans(True))
    