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
        self.program = [1,330,331,332,109,2608,1102,1182,1,16,1101,1399,0,24,102,1,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1105,1,18,1008,571,0,571,1001,16,1,16,1008,16,1399,570,1006,570,14,21102,1,58,0,1105,1,786,1006,332,62,99,21102,333,1,1,21101,0,73,0,1106,0,579,1101,0,0,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,102,1,574,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1106,0,81,21102,340,1,1,1105,1,177,21101,0,477,1,1106,0,177,21102,514,1,1,21101,0,176,0,1106,0,579,99,21101,184,0,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,1001,572,0,1182,21101,375,0,1,21101,211,0,0,1106,0,579,21101,1182,11,1,21102,222,1,0,1105,1,979,21102,388,1,1,21101,0,233,0,1105,1,579,21101,1182,22,1,21101,0,244,0,1105,1,979,21101,401,0,1,21101,0,255,0,1105,1,579,21101,1182,33,1,21101,266,0,0,1105,1,979,21101,0,414,1,21101,0,277,0,1105,1,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21101,1182,0,1,21102,313,1,0,1105,1,622,1005,575,327,1101,1,0,575,21102,327,1,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,4,0,0,109,4,2101,0,-3,587,20101,0,0,-1,22101,1,-3,-3,21101,0,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2106,0,0,109,5,2101,0,-4,629,21002,0,1,-2,22101,1,-4,-4,21102,0,1,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20101,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21101,702,0,0,1105,1,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,1,731,0,1105,1,786,1105,1,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,756,0,0,1106,0,786,1105,1,774,21202,-1,-11,1,22101,1182,1,1,21101,0,774,0,1105,1,622,21201,-3,1,-3,1106,0,640,109,-5,2105,1,0,109,7,1005,575,802,21002,576,1,-6,21002,577,1,-5,1106,0,814,21101,0,0,-1,21102,1,0,-5,21101,0,0,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,39,-3,22201,-6,-3,-3,22101,1399,-3,-3,1202,-3,1,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1105,1,924,1205,-2,873,21102,35,1,-4,1105,1,924,1202,-3,1,878,1008,0,1,570,1006,570,916,1001,374,1,374,2101,0,-3,895,1101,2,0,0,2102,1,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20101,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,39,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,31,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,0,1,575,21102,973,1,0,1105,1,786,99,109,-7,2105,1,0,109,6,21102,0,1,-4,21101,0,0,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1105,1,1041,21102,1,-4,-2,1105,1,1041,21102,-5,1,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,2101,0,-2,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,2101,0,-2,0,1106,0,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21102,1,439,1,1105,1,1150,21102,1,477,1,1106,0,1150,21101,514,0,1,21102,1149,1,0,1105,1,579,99,21101,0,1157,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,2101,0,-4,0,109,-6,2106,0,0,0,5,34,1,38,1,38,1,38,11,3,11,24,1,3,1,34,1,3,1,34,1,3,1,30,5,3,1,30,1,7,1,30,1,7,1,1,11,3,9,6,1,7,1,1,1,9,1,3,1,7,1,6,5,3,5,7,1,3,1,7,1,10,1,5,1,1,1,7,1,3,1,7,1,4,5,1,1,5,1,1,1,7,5,7,1,4,1,3,1,1,1,5,1,1,1,19,1,4,1,3,1,1,1,3,5,19,1,4,1,3,1,1,1,3,1,1,1,21,1,4,1,3,11,19,1,4,1,5,1,3,1,1,1,1,1,19,12,1,5,1,1,15,6,3,1,7,1,1,1,3,1,15,1,4,1,3,1,7,1,1,1,3,1,15,1,4,1,3,1,7,1,1,1,3,1,15,1,4,5,7,11,11,1,18,1,3,1,3,1,11,1,18,11,9,1,22,1,3,1,1,1,9,1,22,5,1,1,9,1,28,1,9,1,28,11,4]
    
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


inpipe = pipe()
outpipe = pipe()
computer = computer(inpipe,outpipe, False)
map = {}
x = 0
y = 0
while not computer.finished:
    if (len(outpipe.buf) >0):
        character = str(chr(outpipe.next()))
        if character == str(chr(10)):
            y += 1
            x = 0
        else:            
            map[(x,y)] = character
            x += 1
    computer.calculate()
buf = ""
for y in range(0,max(k[1] for k,v in map.items())+1):
    for x in range(0, max(k[0] for k,v in map.items())+1):
        buf += map[(x,y)]
    buf += '\n'

print(buf)

inters = 0
for y in range(0,max(k[1] for k,v in map.items())):
    for x in range(0, max(k[0] for k,v in map.items())):
        if (x+1,y) not in map or (x,y+1) not in map or (x-1,y) not in map or (x,y-1) not in map:
            continue
        if map[(x,y)] == '#' and map[(x+1,y)] == '#' and map[(x,y+1)] == '#' and map[(x-1,y)] == '#' and map[(x,y-1)] == '#':
            inters += x*y
print(inters)