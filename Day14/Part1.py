from math import gcd,ceil
reactions = [x.replace('\n','') for x in open('Day14/input.txt').readlines()]
reactions = [[y.strip() for y in x.split('=>')] for x in reactions]
reactions = [(x[0].split(', '), x[1].split(' ')) for x in reactions]
reactions = [([(int(y.split(' ')[0]), y.split(' ')[1].strip()) for y in x[0]], (int(x[1][0]),x[1][1].strip())) for x in reactions]

def compute_lcm(x, y):
   return int((x*y)/gcd(x,y))

def find_component(target):
    return [x for x in reactions if x[1][1] == target][0]

search_stack = [(1, 'FUEL')]
surpluses = {}
ore_cost = 0
while len(search_stack) > 0:
    top = search_stack[0]
    if top[1] in surpluses:
        if top[0] >= surpluses[top[1]]:
            top = (top[0] - surpluses[top[1]],top[1])
            surpluses[top[1]] = 0
        elif top[0] < surpluses[top[1]]:
            surpluses[top[1]] -= top[0]
            search_stack = search_stack[1:]
            continue
    if top[1] == "ORE":
        ore_cost += top[0]
        search_stack = search_stack[1:]
        continue
    rules = find_component(top[1])
    mult = ceil(top[0]/rules[1][0])
    if top[1] not in surpluses:
        surpluses[top[1]] = 0
    surpluses[top[1]] += mult*rules[1][0]-top[0]
    for rule in rules[0]:
        search_stack.append((mult*rule[0],rule[1]))
        pass
    search_stack = search_stack[1:]

print(ore_cost)
pass
