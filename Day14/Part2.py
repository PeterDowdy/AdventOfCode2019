from math import gcd,ceil
reactions = [x.replace('\n','') for x in open('Day14/input.txt').readlines()]
reactions = [[y.strip() for y in x.split('=>')] for x in reactions]
reactions = [(x[0].split(', '), x[1].split(' ')) for x in reactions]
reactions = [([(int(y.split(' ')[0]), y.split(' ')[1].strip()) for y in x[0]], (int(x[1][0]),x[1][1].strip())) for x in reactions]

def compute_lcm(x, y):
   return int((x*y)/gcd(x,y))

def find_component(target):
    return [x for x in reactions if x[1][1] == target][0]

ore_cost = 0
search_stack = [(1, 'FUEL')]
surpluses = {}
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

guesses = {}
max_guess = 2*1000000000000/ore_cost
fuel_amount = int(1000000000000/(ore_cost*2))
while True:
    if fuel_amount in guesses:
        print(f'Found answer: {guesses[fuel_amount]}')
        break
    ore_cost = 0
    search_stack = [(fuel_amount, 'FUEL')]
    surpluses = {}
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
    guesses[fuel_amount] = ore_cost
    guess_keys = list(guesses.keys()).copy()
    guess_keys.append(max_guess)
    guess_keys.append(0)
    if ore_cost < 1000000000000:
        fuel_amount = int((min([x for x in guess_keys if x > fuel_amount])+fuel_amount)/2)
    else:
        fuel_amount = int((fuel_amount+max([x for x in guess_keys if x < fuel_amount]))/2)


