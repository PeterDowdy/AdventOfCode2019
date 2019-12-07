import itertools

def get_opcode(code):
    strcode = str(code)
    while len(strcode) < 5:
        strcode = '0' + strcode
    return (int(strcode[0]), int(strcode[1]), int(strcode[2]), int(strcode[3])*10+int(strcode[4]))
    
def calculate(inputs):
    output = 0
    program = [3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,126,207,288,369,450,99999,3,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,102,5,9,9,1001,9,2,9,102,2,9,9,101,3,9,9,1002,9,2,9,4,9,99,3,9,101,5,9,9,102,5,9,9,1001,9,2,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,5,9,1001,9,5,9,1002,9,4,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99]
    current_input = 0
    cur = 0
    while program[cur] != 99:
        (_, second_mode, first_mode, opcode) = get_opcode(program[cur])
        
        if opcode == 1:
            arg1 = program[cur+1]
            arg2 = program[cur+2]
            target = program[cur+3]
            value1 = program[arg1] if first_mode == 0 else arg1
            value2 = program[arg2] if second_mode == 0 else arg2
            program[target] = value1+value2
            cur = cur + 4
        elif opcode == 2:
            arg1 = program[cur+1]
            arg2 = program[cur+2]
            target = program[cur+3]
            value1 = program[arg1] if first_mode == 0 else arg1
            value2 = program[arg2] if second_mode == 0 else arg2
            program[target] = value1*value2
            cur = cur + 4
        elif opcode == 3: #input
            target = program[cur+1]
            value1 = program[target] if first_mode == 0 else target
            program[target]=inputs[current_input]
            current_input = current_input + 1
            cur = cur + 2
        elif opcode == 4: #output
            target = program[cur+1]
            value1 = program[target] if first_mode == 0 else target
            output = value1
            cur = cur + 2
        elif opcode == 5:
            arg1 = program[cur+1]
            arg2 = program[cur+2]
            value1 = program[arg1] if first_mode == 0 else arg1
            value2 = program[arg2] if second_mode == 0 else arg2
            cur = value2 if value1 != 0 else cur + 3
        elif opcode == 6:
            arg1 = program[cur+1]
            arg2 = program[cur+2]
            value1 = program[arg1] if first_mode == 0 else arg1
            value2 = program[arg2] if second_mode == 0 else arg2
            cur = value2 if value1 == 0 else cur + 3
        elif opcode == 7:
            arg1 = program[cur+1]
            arg2 = program[cur+2]
            target = program[cur+3]
            value1 = program[arg1] if first_mode == 0 else arg1
            value2 = program[arg2] if second_mode == 0 else arg2
            program[target] = 1 if value1 < value2 else 0
            cur = cur + 4
        elif opcode == 8:
            arg1 = program[cur+1]
            arg2 = program[cur+2]
            target = program[cur+3]
            value1 = program[arg1] if first_mode == 0 else arg1
            value2 = program[arg2] if second_mode == 0 else arg2
            program[target] = 1 if value1 == value2 else 0
            cur = cur + 4
        else:
            raise Exception(program[cur])
    return output#program[0]

permutes = itertools.permutations([0,1,2,3,4])
highest = 0
for permute in permutes:
    A = calculate([permute[0],0])
    B = calculate([permute[1],A])
    C = calculate([permute[2],B])
    D = calculate([permute[3],C])
    E = calculate([permute[4],D])
    highest = max(highest,E)
    print(f'{permute[0]}{permute[1]}{permute[2]}{permute[3]}{permute[4]} yields {E}')

print(highest)