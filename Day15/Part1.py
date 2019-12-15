class pipe(object):
    def __init__(self):
        self.buf = []
        self.last_output = 0
    def next(self):
        element = self.buf[0]
        self.buf = self.buf[1:]
        return element
    def peek(self):
        if len(self.buf) == 0:
            return None
        return self.buf[0]
    def write(self,element):
        self.last_output = element
        self.buf.append(element)
    def get_last_output(self):
        return self.last_output

class computer(object):
    def __init__(self,inpipe, outpipe, debug = False):
        self.debug = debug
        self.total_counter = 0
        self.relative_base = 0
        self.finished = False
        self.waiting_on_input = False
        self.cur = 0
        self.input_pipe = inpipe
        self.output_pipe = outpipe
        self.program = [3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1001,1034,0,1039,1001,1036,0,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,102,1,1034,1039,1001,1036,0,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,1001,1035,0,1040,101,0,1038,1043,101,0,1037,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,1002,1035,1,1040,102,1,1038,1043,1001,1037,0,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,37,1032,1006,1032,165,1008,1040,5,1032,1006,1032,165,1102,1,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,64,1044,1106,0,224,1101,0,0,1044,1105,1,224,1006,1044,247,1002,1039,1,1034,101,0,1040,1035,102,1,1041,1036,102,1,1043,1038,101,0,1042,1037,4,1044,1106,0,0,13,40,97,1,18,1,79,93,56,16,38,41,78,11,78,25,46,84,31,38,76,17,96,5,78,50,8,67,77,54,42,82,39,2,8,5,11,85,37,93,37,7,97,12,94,2,44,70,74,78,34,45,94,75,19,8,84,72,2,9,69,74,6,11,75,79,42,35,86,83,23,82,88,40,81,70,8,58,46,57,77,65,76,68,79,61,24,80,61,88,70,42,32,71,16,23,99,77,73,57,45,99,39,29,97,4,90,76,3,5,86,11,95,94,90,59,13,37,94,29,57,42,99,4,45,96,22,74,33,73,70,24,96,4,82,10,3,79,37,81,97,72,42,66,3,27,98,4,73,49,55,86,12,41,65,38,21,66,27,80,87,53,86,26,85,80,42,26,92,17,79,76,58,69,2,71,7,88,12,61,73,16,67,48,83,87,8,21,72,67,50,70,7,71,9,53,46,81,99,47,3,70,11,23,68,22,86,43,32,92,30,78,94,61,81,32,60,89,97,58,23,27,52,99,85,90,41,20,11,87,73,57,83,30,79,2,58,93,32,81,16,86,35,87,38,73,88,11,6,65,32,20,81,87,89,12,11,66,42,84,12,79,14,23,72,37,85,95,15,48,80,92,59,56,7,95,85,21,82,53,93,45,73,29,79,6,17,68,79,34,72,47,39,81,93,63,83,51,67,99,1,74,56,89,47,86,95,51,94,46,3,95,18,81,20,85,19,90,60,24,65,65,46,91,17,82,37,87,21,83,80,22,28,75,17,68,72,40,67,82,19,9,79,42,86,55,93,91,41,76,55,22,74,61,91,42,96,73,11,1,79,60,85,82,40,76,88,84,2,14,97,89,29,69,39,43,65,19,58,97,68,45,50,2,91,54,52,93,82,61,76,22,15,77,63,76,60,81,42,89,77,45,80,3,92,17,10,98,16,92,38,71,2,46,81,81,11,7,43,82,68,82,93,25,44,87,60,49,48,7,47,82,82,26,65,93,50,75,57,92,57,78,11,39,99,2,93,42,69,6,66,60,96,79,50,20,75,84,48,98,57,5,93,98,62,78,85,53,85,32,37,90,90,30,43,74,57,81,19,35,19,94,50,65,60,98,65,46,86,75,68,16,31,83,75,56,93,35,42,89,32,69,35,2,60,82,58,53,1,87,18,66,82,41,73,73,7,99,91,89,48,83,20,81,31,66,17,93,23,41,86,65,57,72,13,13,82,94,79,77,54,89,90,62,95,35,74,82,37,43,33,66,77,3,86,26,87,35,69,19,24,85,62,18,9,72,42,69,25,95,57,34,41,82,36,90,24,36,27,67,49,30,70,75,82,44,33,67,70,35,36,69,33,85,10,87,50,72,8,74,97,18,95,25,97,5,84,16,65,60,89,15,86,81,9,75,73,58,72,39,91,10,55,3,11,86,96,18,98,97,28,22,98,49,89,19,84,18,98,34,92,67,37,80,17,8,65,72,2,91,95,55,76,19,30,78,40,96,78,34,91,99,23,14,71,38,37,71,59,93,78,83,61,24,31,97,25,85,8,16,84,15,65,77,14,96,98,6,89,33,98,59,4,84,66,18,74,48,12,41,86,31,45,33,74,97,86,55,85,16,34,54,91,77,3,19,65,70,18,90,41,98,25,55,22,95,15,92,14,67,20,88,5,51,69,92,33,69,75,56,36,91,3,80,13,78,36,88,50,88,79,65,24,66,5,99,45,98,88,66,30,92,98,84,5,90,13,67,95,96,33,77,30,80,39,99,81,95,55,86,0,0,21,21,1,10,1,0,0,0,0,0,0]
    
    def write_positional(self,position,argument):
        while position >= len(self.program):
            self.program.append(0)
        self.program[position] = argument
    
    def read_positional(self,position):
        while position >= len(self.program):
            self.program.append(0)
        return self.program[position]
    
    def read_absolute(self,position):
        return position
    
    def write_relative_base(self,position,argument):
        while position+self.relative_base >= len(self.program):
            self.program.append(0)
        self.program[position+self.relative_base] = argument
    
    def read_relative_base(self,position):
        while position+self.relative_base >= len(self.program):
            self.program.append(0)
        return self.program[position+self.relative_base]
    
    def get_accessors(self,mode):
        if mode == 0: #positional mode
            return (lambda a,b: self.write_positional(a,b),lambda a: self.read_positional(a))
        if mode == 1: #absolute mode
            return (lambda a,b: None,lambda a: self.read_absolute(a))
        if mode == 2: #relative base mode
            return (lambda a,b: self.write_relative_base(a,b), lambda a: self.read_relative_base(a))

    def get_opcode(self,code):
        strcode = str(code)
        while len(strcode) < 5:
            strcode = '0' + strcode
        return (int(strcode[0]), int(strcode[1]), int(strcode[2]), int(strcode[3])*10+int(strcode[4]))
    def is_finished(self):
        return self.finished
    def calculate(self):
        self.total_counter = self.total_counter + 1
        if self.program[self.cur] == 99:
            if self.debug: print('Exit')
            self.finished = True
            return
        while self.cur+3 >= len(self.program):
            self.program.append(0)
        (third_mode, second_mode, first_mode, opcode) = self.get_opcode(self.program[self.cur])
        if self.debug: print(f'[{self.total_counter}|{self.cur}]: {self.program[self.cur]} = first:{"positional" if first_mode == 0 else "absolute" if first_mode == 1 else "relative base"}, second:{"positional" if second_mode == 0 else "absolute" if second_mode == 1 else "relative base"}, third:{"positional" if third_mode == 0 else "absolute" if third_mode == 1 else "relative base"} opcode:{opcode}')
        first_accessors = self.get_accessors(first_mode)
        (first_write,first_read) = first_accessors
        second_accessors = self.get_accessors(second_mode)
        (second_write,second_read) = second_accessors
        third_accessors = self.get_accessors(third_mode)
        third_write, third_read = third_accessors
        first_node = self.program[self.cur+1]
        second_node = self.program[self.cur+2]
        third_node = self.program[self.cur+3]
        if opcode == 1:
            if self.debug: print('add')
            if self.debug: print(f'{self.program[self.cur]},{self.program[self.cur+1]},{self.program[self.cur+2]},{self.program[self.cur+3]}')
            third_write(third_node, first_read(first_node)+second_read(second_node))
            if self.debug: print(f'{first_read(first_node)}+{second_read(second_node)}->program[{third_node}]')
            self.cur = self.cur + 4
        elif opcode == 2:
            if self.debug: print('multiply')
            if self.debug: print(f'{self.program[self.cur]},{self.program[self.cur+1]},{self.program[self.cur+2]},{self.program[self.cur+3]}')
            third_write(third_node, first_read(first_node)*second_read(second_node))
            if self.debug: print(f'{first_read(first_node)}*{second_read(second_node)}->program[{third_node}]')
            self.cur = self.cur + 4
        elif opcode == 3: #input
            if self.debug: print('input')
            if self.debug: print(f'{self.program[self.cur]},{self.program[self.cur+1]}')
            if self.input_pipe.peek() is None:
                self.waiting_on_input = True
                return
            self.waiting_on_input = False
            next_input = self.input_pipe.next()
            first_write(first_node,next_input)
            if self.debug: print(f'input:{next_input}')
            self.cur = self.cur + 2
        elif opcode == 4: #output
            if self.debug: print('output')
            if self.debug: print(f'{self.program[self.cur]},{self.program[self.cur+1]}')
            output_value = first_read(first_node)
            self.output_pipe.write(output_value)
            if self.debug: print(f'out: {output_value}')
            self.cur = self.cur + 2
        elif opcode == 5: #jump if not zero
            if self.debug: print('jump if not zero')
            if self.debug: print(f'{self.program[self.cur]},{self.program[self.cur+1]},{self.program[self.cur+2]}')
            self.cur = second_read(second_node) if first_read(first_node) != 0 else self.cur + 3
            if self.debug:
                if first_read(first_node) != 0: print(f'{first_read(first_node)} != 0, cur = {second_read(second_node)}')
                else: print(f'{first_read(first_node)} == 0, no jump')
        elif opcode == 6: #jump if zero
            if self.debug: print('jump if zero')
            if self.debug: print(f'{self.program[self.cur]},{self.program[self.cur+1]},{self.program[self.cur+2]}')
            self.cur = second_read(second_node) if first_read(first_node) == 0 else self.cur + 3
            if self.debug:
                if first_read(first_node) == 0: print(f'{first_read(first_node)} == 0, cur = {second_read(second_node)}')
                else: print(f'{first_read(first_node)} != 0, no jump')
        elif opcode == 7: #less than
            if self.debug: print('less than')
            if self.debug: print(f'{self.program[self.cur]},{self.program[self.cur+1]},{self.program[self.cur+2]},{self.program[self.cur+3]}')
            third_write(third_node, 1 if first_read(first_node) < second_read(second_node) else 0)
            if self.debug:
                if first_read(first_node) < second_read(second_node): print(f'{first_read(first_node)} < {second_read(second_node)}, position {third_node} = 1')
                else: print(f'{first_read(first_node)} >= {second_read(second_node)}, position {third_node} = 0')
            self.cur = self.cur + 4
        elif opcode == 8: #equal
            if self.debug: print('equal')
            if self.debug: print(f'{self.program[self.cur]},{self.program[self.cur+1]},{self.program[self.cur+2]},{self.program[self.cur+3]}')
            third_write(third_node, 1 if first_read(first_node) == second_read(second_node) else 0)
            if self.debug:
                if first_read(first_node) == second_read(second_node): print(f'{first_read(first_node)} == {second_read(second_node)}, position {third_node} = 1')
                else: print(f'{first_read(first_node)} != {second_read(second_node)}, position {third_node} = 0')
            self.cur = self.cur + 4
        elif opcode == 9:
            if self.debug: print('alter relative base')
            if self.debug: print(f'{self.program[self.cur]},{self.program[self.cur+1]}')
            if self.debug:
                print(f'relative base {self.relative_base} +/- {first_read(first_node)} = {self.relative_base+first_read(first_node)}')
            self.relative_base = self.relative_base+first_read(first_node)
            self.cur = self.cur + 2
        else:
            raise Exception(self.program[self.cur])
import os
from math import sqrt

def next_move(path,map):
    current = path[-1]
    candidates = []
    for neighbour in [
        (current[0]+1,current[1]),
        (current[0],current[1]+1),
        (current[0]-1,current[1]),
        (current[0],current[1]-1)
    ]:
        if neighbour in path:
            pass
        elif neighbour not in map:
            candidates.append(path + [neighbour])
        elif map[neighbour] == '#':
            pass
        else:
            child_path = next_move(path + [neighbour], map)
            if child_path is not None:
                candidates.append(child_path)
    if len(candidates) == 0:
        return None
    return sorted(candidates, key=lambda x: len(x))[0]
draw_cycle = 1
map = {(0,0): '.'}
droid_position = (0,0)
droid_new_position = droid_position
inpipe = pipe()
outpipe = pipe()
computer = computer(inpipe,outpipe, False)
move_buf = []
while not computer.finished:
    direction = -1
    if computer.waiting_on_input:
        if len(move_buf) == 0:
            next_moves = next_move([droid_position],map)
            for step in range(0,len(next_moves)-1):
                if next_moves[step][1] < next_moves[step+1][1]:
                    move_buf.append(1)
                if next_moves[step][1] > next_moves[step+1][1]:
                    move_buf.append(2)
                if next_moves[step][0] > next_moves[step+1][0]:
                    move_buf.append(3)
                if next_moves[step][0] < next_moves[step+1][0]:
                    move_buf.append(4)
        instruction = move_buf[0]
        inpipe.write(instruction)
        move_buf = move_buf[1:]
        if instruction == 1:
            droid_new_position = (droid_position[0],droid_position[1]+1)
        if instruction == 2:
            droid_new_position = (droid_position[0],droid_position[1]-1)
        if instruction == 3:
            droid_new_position = (droid_position[0]-1,droid_position[1])
        if instruction == 4:
            droid_new_position = (droid_position[0]+1,droid_position[1])
    if (len(outpipe.buf) > 0):
        response = outpipe.next()
        if response == 0:
            map[droid_new_position] = '#'
        if response == 1:
            map[droid_new_position] = '.'
            droid_position = droid_new_position
        if response == 2:
            map[droid_new_position] = 'O'
            droid_position = droid_new_position
            computer.finished = True
        
        draw_cycle += 1
        if draw_cycle % 1000 == 0:
            draw_cycle = 1
            os.system('cls' if os.name == 'nt' else 'clear')
            buf = ''
            for y in range(1+max([k[1] for k,v in map.items()]),min([k[1] for k,v in map.items()])-1,-1):
                for x in range(min([k[0] for k,v in map.items()])-1,1+max([k[0] for k,v in map.items()])):
                    if droid_position == (x,y):
                        buf += 'X'
                    elif (x,y) in map:
                        buf += map[(x,y)]
                    else:
                        buf += ' '
                buf += "\n"
            print(buf)
    computer.calculate()
os.system('cls' if os.name == 'nt' else 'clear')
buf = ''
for y in range(1+max([k[1] for k,v in map.items()]),min([k[1] for k,v in map.items()])-1,-1):
    for x in range(min([k[0] for k,v in map.items()])-1,1+max([k[0] for k,v in map.items()])):
        #if droid_position == (x,y):
        #    buf += 'X'
        if (x,y) == (0,0):
            buf += 'S'
        elif (x,y) in map:
            buf += map[(x,y)]
        else:
            buf += ' '
    buf += "\n"
print(buf)

def find_path(path,goal,map):
    current = path[-1]
    candidates = []
    for neighbour in [
        (current[0]+1,current[1]),
        (current[0],current[1]+1),
        (current[0]-1,current[1]),
        (current[0],current[1]-1)
    ]:
        if neighbour in path:
            pass
        elif neighbour not in map:
            pass
        elif map[neighbour] == '#':
            pass
        elif map[neighbour] == 'O':
            return path + [neighbour]
        else:
            child_path = find_path(path + [neighbour], goal, map)
            if child_path is not None:
                candidates.append(child_path)
    if len(candidates) == 0:
        return None
    return sorted(candidates, key=lambda x: len(x))[0]

shortest_path = find_path([(0,0)],[k for k,v in map.items() if v == 'O'][0],map)
print(f'shortest path needs {len(shortest_path)-1} steps')