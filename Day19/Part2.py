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
        self.program = [109,424,203,1,21102,1,11,0,1105,1,282,21102,18,1,0,1106,0,259,2102,1,1,221,203,1,21102,31,1,0,1105,1,282,21101,38,0,0,1106,0,259,21002,23,1,2,22101,0,1,3,21102,1,1,1,21101,57,0,0,1105,1,303,1202,1,1,222,20102,1,221,3,20102,1,221,2,21102,1,259,1,21102,80,1,0,1105,1,225,21102,72,1,2,21101,91,0,0,1105,1,303,1201,1,0,223,20102,1,222,4,21101,0,259,3,21102,1,225,2,21102,1,225,1,21102,1,118,0,1105,1,225,20102,1,222,3,21101,104,0,2,21101,0,133,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21102,148,1,0,1106,0,259,1201,1,0,223,20101,0,221,4,20102,1,222,3,21101,0,18,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,106,0,109,20207,1,223,2,20101,0,23,1,21102,1,-1,3,21102,214,1,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2102,1,-4,249,22102,1,-3,1,22102,1,-2,2,22102,1,-1,3,21101,250,0,0,1105,1,225,22102,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21202,-2,1,3,21101,0,343,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,384,1,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2105,1,0]
    
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

import heapq


pointsmap = {}
points_to_scan = []

def find_point(next_point):
    global points_to_scan
    global pointsmap
    inpipe = pipe()
    outpipe = pipe()
    thiscomputer = computer(inpipe,outpipe, False)
    while not thiscomputer.finished:
        if thiscomputer.waiting_on_input:
            inpipe.write(next_point[0])
            inpipe.write(next_point[1])
        if len(outpipe.buf) > 0:
            pointsmap[next_point] = outpipe.next()
            if pointsmap[next_point] == 1:
                heapq.heappush(points_to_scan, ((next_point[0]+1)**2+(next_point[1]+1)**2,next_point[0]+1,next_point[1]+1))
                heapq.heappush(points_to_scan, ((next_point[0]+1)**2+(next_point[1])**2,next_point[0]+1,next_point[1]))
                heapq.heappush(points_to_scan, ((next_point[0]+1)**2+(next_point[1]-1)**2,next_point[0]+1,next_point[1]-1))
                heapq.heappush(points_to_scan, ((next_point[0])**2+(next_point[1]-1)**2,next_point[0],next_point[1]-1))
                heapq.heappush(points_to_scan, ((next_point[0])**2+(next_point[1]+1)**2,next_point[0],next_point[1]+1))
                heapq.heappush(points_to_scan, ((next_point[0]-1)**2+(next_point[1]-1)**2,next_point[0]-1,next_point[1]-1))
                heapq.heappush(points_to_scan, ((next_point[0]-1)**2+(next_point[1])**2,next_point[0]-1,next_point[1]))
        thiscomputer.calculate()

def contains_target(next_point):
    find_point((next_point[0]+100,next_point[1]))
    find_point((next_point[0],next_point[1]+100))
    find_point((next_point[0]+100,next_point[1]+100))
    if pointsmap[next_point] == 1 and pointsmap[(next_point[0]+100,next_point[1])] == 1 and pointsmap[(next_point[0],next_point[1]+100)] == 1 and pointsmap[(next_point[0]+100,next_point[1]+100)] == 1:
        buf = ""
        for y in range(0, max([k[1] for k,v in pointsmap.items()])):
            for x in range(0, max([k[0] for k,v in pointsmap.items()])):
                if (x,y) not in pointsmap: buf += ' '
                elif pointsmap[(x,y)] == 1: buf += '#'
                else: buf += '.'
            buf += '\n'
        print(buf)
        print(next_point)
        print(next_point[0]*10000+next_point[1])
        exit()



for x in range(0,10):
    for y in range(0,10):
        heapq.heappush(points_to_scan, (x**2+y**2,x,y))
while (len(points_to_scan) > 0):
    next_point = heapq.heappop(points_to_scan)
    if (next_point[1],next_point[2]) in pointsmap:
        continue
    find_point((next_point[1],next_point[2]))
    contains_target((next_point[1],next_point[2]))
