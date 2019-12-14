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
        self.program = [1,380,379,385,1008,2663,456801,381,1005,381,12,99,109,2664,1101,0,0,383,1101,0,0,382,20101,0,382,1,20102,1,383,2,21102,37,1,0,1105,1,578,4,382,4,383,204,1,1001,382,1,382,1007,382,44,381,1005,381,22,1001,383,1,383,1007,383,23,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1106,0,161,107,1,392,381,1006,381,161,1101,-1,0,384,1106,0,119,1007,392,42,381,1006,381,161,1102,1,1,384,21001,392,0,1,21102,1,21,2,21102,1,0,3,21102,138,1,0,1105,1,549,1,392,384,392,21001,392,0,1,21101,0,21,2,21102,1,3,3,21101,0,161,0,1106,0,549,1101,0,0,384,20001,388,390,1,20101,0,389,2,21102,1,180,0,1105,1,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,21001,389,0,2,21101,0,205,0,1106,0,393,1002,390,-1,390,1102,1,1,384,20102,1,388,1,20001,389,391,2,21102,1,228,0,1105,1,578,1206,1,261,1208,1,2,381,1006,381,253,20101,0,388,1,20001,389,391,2,21102,1,253,0,1105,1,393,1002,391,-1,391,1101,1,0,384,1005,384,161,20001,388,390,1,20001,389,391,2,21102,1,279,0,1105,1,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21101,0,304,0,1105,1,393,1002,390,-1,390,1002,391,-1,391,1102,1,1,384,1005,384,161,21001,388,0,1,20102,1,389,2,21102,1,0,3,21101,338,0,0,1105,1,549,1,388,390,388,1,389,391,389,20102,1,388,1,20102,1,389,2,21102,1,4,3,21101,0,365,0,1106,0,549,1007,389,22,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,315,20,18,1,1,22,109,3,22101,0,-2,1,21202,-1,1,2,21102,0,1,3,21101,0,414,0,1106,0,549,22102,1,-2,1,21202,-1,1,2,21101,429,0,0,1106,0,601,1202,1,1,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2105,1,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,21202,-3,1,-7,109,-8,2106,0,0,109,4,1202,-2,44,566,201,-3,566,566,101,639,566,566,2102,1,-1,0,204,-3,204,-2,204,-1,109,-4,2106,0,0,109,3,1202,-1,44,594,201,-2,594,594,101,639,594,594,20101,0,0,-2,109,-3,2106,0,0,109,3,22102,23,-2,1,22201,1,-1,1,21102,1,509,2,21101,264,0,3,21102,1012,1,4,21102,1,630,0,1106,0,456,21201,1,1651,-2,109,-3,2106,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,2,0,0,2,0,2,0,0,2,0,2,0,0,2,2,0,2,0,2,2,0,0,0,0,2,0,0,2,2,2,0,2,0,2,0,2,2,2,0,1,1,0,0,0,2,2,0,0,0,0,2,2,2,0,0,2,0,2,0,0,0,0,2,2,2,2,0,0,2,0,2,2,2,2,0,0,0,2,0,2,0,0,0,1,1,0,2,0,0,0,2,0,2,2,2,0,0,2,0,2,0,0,0,0,2,2,0,0,2,2,0,0,2,0,0,0,0,2,2,0,2,0,0,2,0,0,0,1,1,0,0,2,0,2,2,0,0,0,2,0,2,2,2,0,2,0,2,2,2,2,0,2,2,2,0,0,0,0,0,2,0,2,0,2,0,2,2,0,0,2,0,1,1,0,0,0,0,0,2,0,2,2,0,0,2,0,2,0,2,2,0,0,0,0,2,2,0,2,2,2,0,2,2,0,2,2,0,0,2,2,0,0,0,2,0,1,1,0,0,2,2,2,0,0,0,0,0,2,2,0,0,2,0,0,0,2,2,0,2,2,0,0,2,0,0,2,0,0,0,2,2,0,2,2,2,0,2,0,0,1,1,0,0,2,0,0,2,0,2,2,2,2,2,0,2,0,0,0,0,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,0,2,0,0,0,2,2,2,0,1,1,0,2,0,0,2,2,2,0,2,2,2,0,2,2,0,0,0,2,0,2,2,0,2,0,2,2,2,0,2,0,0,0,0,0,0,2,0,2,2,2,2,0,1,1,0,0,2,2,2,2,0,2,2,2,2,0,2,2,2,0,0,0,2,0,0,0,0,0,2,2,2,2,2,2,0,0,2,0,2,2,2,2,2,0,0,0,1,1,0,0,2,2,2,2,2,0,0,2,2,0,0,2,2,0,2,0,0,0,0,2,2,0,2,0,2,2,2,2,0,2,0,0,2,2,0,2,2,0,2,0,1,1,0,2,0,2,2,0,0,2,0,2,0,2,2,0,2,0,2,0,2,2,0,0,2,2,2,2,0,2,2,2,0,2,2,0,0,0,2,2,0,0,2,0,1,1,0,2,0,0,2,2,2,2,2,0,0,2,0,0,2,2,2,0,2,0,2,0,2,0,0,0,2,0,0,0,0,2,2,2,2,0,2,2,0,0,0,0,1,1,0,0,2,0,0,2,2,0,2,0,2,0,2,2,0,0,2,0,2,0,0,2,2,2,2,2,2,0,0,0,0,2,2,2,2,2,0,2,0,2,2,0,1,1,0,0,0,2,2,2,2,2,2,2,0,0,2,0,0,0,0,2,0,2,2,2,2,0,2,0,2,0,0,2,0,2,2,2,2,0,0,0,2,2,2,0,1,1,0,0,0,2,2,0,2,0,2,2,0,2,0,2,0,0,0,2,0,2,0,2,2,0,2,0,0,2,0,0,2,0,2,0,2,2,2,0,0,2,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,78,97,10,89,31,40,53,97,63,60,92,10,54,27,53,42,36,34,79,30,8,70,22,20,18,67,79,30,81,50,67,46,39,15,72,26,35,61,6,36,2,26,65,94,82,27,37,6,71,66,84,19,69,5,62,89,57,49,1,9,59,67,30,74,71,37,66,77,43,4,59,42,85,4,87,1,24,64,85,25,29,67,97,15,22,6,34,97,97,47,22,19,40,89,45,36,93,77,26,85,30,40,65,21,45,91,18,77,45,13,74,18,47,67,79,1,31,22,1,96,94,60,44,56,79,64,74,56,91,79,41,23,9,57,9,86,63,82,55,92,63,63,94,73,76,40,88,18,26,66,29,27,20,1,94,90,43,11,67,33,27,47,34,73,65,67,77,54,92,84,6,29,41,8,8,38,83,36,74,29,26,70,68,57,54,38,75,37,24,64,30,89,43,61,6,4,65,81,39,85,91,22,28,17,47,95,52,40,76,77,81,52,59,19,37,90,23,33,5,82,3,64,46,70,22,24,9,96,97,69,48,66,58,97,51,15,86,6,23,7,35,52,57,3,79,82,71,87,64,91,93,69,77,95,1,57,5,2,65,35,57,14,35,12,14,60,45,52,67,32,26,93,63,54,45,8,48,83,5,49,95,60,78,98,54,62,9,1,39,57,63,82,52,90,64,38,95,8,12,72,22,53,78,63,72,65,59,1,87,95,81,79,38,92,61,60,59,3,39,31,47,69,70,6,55,44,49,54,49,50,11,87,85,89,15,70,58,5,87,65,79,86,92,98,49,73,8,79,30,55,4,30,11,55,80,28,63,28,33,9,49,70,34,83,29,97,67,65,89,50,88,29,40,5,3,11,87,85,43,2,51,18,58,39,81,8,15,2,42,95,64,8,76,60,73,67,30,28,11,84,56,73,14,66,43,21,40,31,48,11,65,27,9,37,60,91,34,11,83,45,9,77,70,97,9,13,68,20,17,15,6,13,44,59,51,91,73,60,37,40,18,69,48,14,44,96,71,21,27,90,9,91,14,80,38,69,69,52,28,15,54,63,46,32,78,54,79,95,83,16,44,29,26,92,31,51,66,14,94,49,1,93,43,57,50,82,45,95,83,74,50,87,47,55,62,31,1,88,1,77,59,64,26,48,22,61,56,20,54,59,62,3,59,28,98,45,53,47,72,73,72,43,30,23,94,10,76,63,63,8,30,92,25,61,61,32,64,25,57,61,95,81,23,67,28,59,48,68,21,85,48,32,93,98,50,89,27,46,38,63,38,87,76,76,10,71,36,91,2,47,2,36,37,90,25,97,27,71,67,77,4,11,57,68,87,94,12,83,91,94,92,35,49,46,4,31,64,39,12,92,26,12,75,29,11,5,83,8,23,73,62,74,55,75,38,40,90,73,71,38,15,75,10,38,55,74,82,13,32,55,90,47,6,25,65,88,85,40,13,66,54,39,82,19,15,18,74,19,54,70,30,56,28,2,20,50,44,51,7,4,79,97,90,71,97,5,25,95,22,36,61,30,16,68,61,23,22,60,93,9,92,98,40,41,11,47,7,57,15,51,51,77,22,32,4,27,10,76,76,50,81,96,46,28,38,69,41,43,47,86,66,54,22,33,45,75,75,51,37,62,62,25,71,35,49,93,44,18,92,39,32,11,31,96,2,33,94,45,14,82,57,79,81,57,6,19,63,35,11,55,18,38,22,43,82,76,35,7,21,74,50,83,7,55,94,23,79,85,20,4,65,18,12,62,35,74,23,20,96,71,25,95,45,95,4,18,82,71,79,4,12,41,44,23,8,86,6,78,5,54,68,60,12,73,18,95,31,86,23,5,36,40,97,35,48,28,15,9,27,54,14,22,97,63,41,37,12,20,38,41,27,70,35,10,89,31,90,44,46,44,49,66,71,58,74,7,24,6,96,68,27,16,89,80,1,38,26,88,60,47,27,46,32,34,44,74,51,70,13,57,14,31,40,71,55,22,87,23,9,37,38,18,17,34,84,84,49,74,81,31,4,45,11,71,89,16,56,91,61,61,67,92,14,88,89,10,11,77,38,40,89,76,7,5,74,54,64,97,25,20,1,41,9,41,97,1,31,21,96,98,88,52,71,25,62,42,8,91,84,43,75,37,22,32,58,87,22,6,13,62,48,85,81,48,70,3,13,93,88,52,7,66,84,27,37,21,62,72,40,30,28,12,88,48,47,96,98,47,76,80,98,42,25,72,13,15,31,81,40,16,85,77,82,41,67,93,73,58,86,68,85,28,60,13,87,9,12,40,20,4,92,51,456801]
    
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

blocks = 0

inpipe = pipe()
outpipe = pipe()
computer = computer(inpipe,outpipe, False)
while not computer.finished:
    if len(outpipe.buf) == 3:
        outpipe.next()
        outpipe.next()
        if outpipe.next() == 2:
            blocks += 1
        pass

    if computer.waiting_on_input:
        pass
    computer.calculate()


print(blocks)
pass