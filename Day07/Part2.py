import itertools

def get_opcode(code):
    strcode = str(code)
    while len(strcode) < 5:
        strcode = '0' + strcode
    return (int(strcode[0]), int(strcode[1]), int(strcode[2]), int(strcode[3])*10+int(strcode[4]))

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

class amplifier(object):
    def __init__(self,inpipe, outpipe):
        self.finished = False
        self.cur = 0
        self.input_pipe = inpipe
        self.output_pipe = outpipe
        self.program = [3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,126,207,288,369,450,99999,3,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,102,5,9,9,1001,9,2,9,102,2,9,9,101,3,9,9,1002,9,2,9,4,9,99,3,9,101,5,9,9,102,5,9,9,1001,9,2,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,5,9,1001,9,5,9,1002,9,4,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99]

    def is_finished(self):
        return self.finished
    def calculate(self):
        if self.program[self.cur] == 99:
            self.finished = True
            return
        (_, second_mode, first_mode, opcode) = get_opcode(self.program[self.cur])
        if opcode == 1:
            arg1 = self.program[self.cur+1]
            arg2 = self.program[self.cur+2]
            target = self.program[self.cur+3]
            value1 = self.program[arg1] if first_mode == 0 else arg1
            value2 = self.program[arg2] if second_mode == 0 else arg2
            self.program[target] = value1+value2
            self.cur = self.cur + 4
        elif opcode == 2:
            arg1 = self.program[self.cur+1]
            arg2 = self.program[self.cur+2]
            target = self.program[self.cur+3]
            value1 = self.program[arg1] if first_mode == 0 else arg1
            value2 = self.program[arg2] if second_mode == 0 else arg2
            self.program[target] = value1*value2
            self.cur = self.cur + 4
        elif opcode == 3: #input
            if self.input_pipe.peek() is None:
                return
            target = self.program[self.cur+1]
            value1 = self.program[target] if first_mode == 0 else target
            self.program[target]=self.input_pipe.next()
            self.cur = self.cur + 2
        elif opcode == 4: #output
            target = self.program[self.cur+1]
            value1 = self.program[target] if first_mode == 0 else target
            self.output_pipe.write(value1)
            self.cur = self.cur + 2
        elif opcode == 5:
            arg1 = self.program[self.cur+1]
            arg2 = self.program[self.cur+2]
            value1 = self.program[arg1] if first_mode == 0 else arg1
            value2 = self.program[arg2] if second_mode == 0 else arg2
            self.cur = value2 if value1 != 0 else self.cur + 3
        elif opcode == 6:
            arg1 = self.program[self.cur+1]
            arg2 = self.program[self.cur+2]
            value1 = self.program[arg1] if first_mode == 0 else arg1
            value2 = self.program[arg2] if second_mode == 0 else arg2
            self.cur = value2 if value1 == 0 else self.cur + 3
        elif opcode == 7:
            arg1 = self.program[self.cur+1]
            arg2 = self.program[self.cur+2]
            target = self.program[self.cur+3]
            value1 = self.program[arg1] if first_mode == 0 else arg1
            value2 = self.program[arg2] if second_mode == 0 else arg2
            self.program[target] = 1 if value1 < value2 else 0
            self.cur = self.cur + 4
        elif opcode == 8:
            arg1 = self.program[self.cur+1]
            arg2 = self.program[self.cur+2]
            target = self.program[self.cur+3]
            value1 = self.program[arg1] if first_mode == 0 else arg1
            value2 = self.program[arg2] if second_mode == 0 else arg2
            self.program[target] = 1 if value1 == value2 else 0
            self.cur = self.cur + 4
        else:
            raise Exception(self.program[self.cur])

permutes = itertools.permutations([5,6,7,8,9])
highest = 0
for permute in permutes:
    AtoB = pipe()
    BtoC = pipe()
    CtoD = pipe()
    DtoE = pipe()
    EtoA = pipe()
    A = amplifier(EtoA,AtoB)
    B = amplifier(AtoB,BtoC)
    C = amplifier(BtoC,CtoD)
    D = amplifier(CtoD,DtoE)
    E = amplifier(DtoE,EtoA)
    EtoA.write(permute[0])
    EtoA.write(0)
    AtoB.write(permute[1])
    BtoC.write(permute[2])
    CtoD.write(permute[3])
    DtoE.write(permute[4])
    while not A.is_finished() or not B.is_finished() or not C.is_finished() or not D.is_finished() or not E.is_finished():
        A.calculate()
        B.calculate()
        C.calculate()
        D.calculate()
        E.calculate()
    highest = max(highest, EtoA.get_last_output())
print(highest)