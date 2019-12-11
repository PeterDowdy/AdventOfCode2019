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
        self.program = [3,8,1005,8,284,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,28,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,50,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,72,1006,0,24,1,1106,12,10,1006,0,96,1,1008,15,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,108,1006,0,54,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,134,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,155,1006,0,60,1006,0,64,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,183,1006,0,6,1006,0,62,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,211,1,108,0,10,2,1002,15,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,242,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,263,101,1,9,9,1007,9,1010,10,1005,10,15,99,109,606,104,0,104,1,21101,0,666526126996,1,21101,301,0,0,1105,1,405,21101,846138811028,0,1,21101,312,0,0,1106,0,405,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,248129978391,1,21101,359,0,0,1105,1,405,21101,97751403560,0,1,21102,1,370,0,1106,0,405,3,10,104,0,104,0,3,10,104,0,104,0,21101,988753585000,0,1,21101,393,0,0,1105,1,405,21102,867961709324,1,1,21102,404,1,0,1106,0,405,99,109,2,22102,1,-1,1,21102,40,1,2,21101,436,0,3,21102,1,426,0,1105,1,469,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,431,432,447,4,0,1001,431,1,431,108,4,431,10,1006,10,463,1102,0,1,431,109,-2,2106,0,0,0,109,4,1202,-1,1,468,1207,-3,0,10,1006,10,486,21102,1,0,-3,22101,0,-3,1,21202,-2,1,2,21102,1,1,3,21101,505,0,0,1106,0,510,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,533,2207,-4,-2,10,1006,10,533,22101,0,-4,-4,1105,1,601,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,552,0,1105,1,510,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,571,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,593,21202,-1,1,1,21102,1,593,0,106,0,468,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
    
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

robot_position = (0,0)
paints = {(0,0): 1}
direction = 'N'

inpipe = pipe()
outpipe = pipe()
computer = computer(inpipe,outpipe, False)
inpipe.write(1)
while not computer.finished:
    if len(outpipe.buf) == 2:
        paints[(robot_position)] = outpipe.next()
        if direction == 'N':
            direction = 'E' if outpipe.next() == 1 else 'W'
        elif direction == 'E':
            direction = 'S' if outpipe.next() == 1 else 'N'
        elif direction == 'S':
            direction = 'W' if outpipe.next() == 1 else 'E'
        elif direction == 'W':
            direction = 'N' if outpipe.next() == 1 else 'S'

        if direction == 'N':
            robot_position = (robot_position[0],robot_position[1]+1)
        if direction == 'E':
            robot_position = (robot_position[0]+1,robot_position[1])
        if direction == 'S':
            robot_position = (robot_position[0],robot_position[1]-1)
        if direction == 'W':
            robot_position = (robot_position[0]-1,robot_position[1])

    if computer.waiting_on_input:
        if robot_position in paints: inpipe.write(paints[robot_position])
        else: inpipe.write(0)
    computer.calculate()

x_min = min([x[0] for x in dict.keys(paints)])
x_max = max([x[0] for x in dict.keys(paints)])
y_min = min([y[1] for y in dict.keys(paints)])
y_max = max([y[1] for y in dict.keys(paints)])
x_min = min(x_min,y_min)
y_min = min(x_min,y_min)
x_max = max(x_max,y_max)
y_max = max(x_max,y_max)
buf = ""
for x in range(x_min,x_max+1):
    for y in range(y_min,y_max+1):
        buf += "#" if (x,y) in paints and paints[(x,y)] == 1 else " "
    buf += "\n"

print(buf)
pass