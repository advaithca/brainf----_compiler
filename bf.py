op = []

class BrainFuck:
    '''
    Class implementing a brainfuck compiler.
    '''
    def __init__(self,memSize):
        '''
        Initialize memory size
        '''
        self.memory = [0]*memSize
        self.ptr = 0
        self.bracePos = dict()

    def __convert(self, code):
        i = []
        k = 0
        code = [x for x in code]
        while k < len(code):
            if code[k] == '[':
                i.append(k)
                code[k] = str(k)
            if code[k] == ']':
                j = i.pop(-1)
                self.bracePos[k] = j
                code[k] = str(j)
            k += 1
        bpdup = self.bracePos.copy()
        for key, val in bpdup.items():
            self.bracePos[val] = key

    def compile(self, code):
        '''
        Provide code that is to be compiled and evaluated
        '''
        self.__convert(code)
        i = 0
        while i < len(code):
            if code[i] == '>':
                self.ptr += 1
                if self.ptr == len(self.memory):
                    self.memory.append(0)

            elif code[i] == '<':
                self.ptr =self.ptr - 1 if self.ptr > 0 else 0

            elif code[i] == '+':
                self.memory[self.ptr] = self.memory[self.ptr] + 1 if self.memory[self.ptr] < 255 else 0

            elif code[i] == '-':
                self.memory[self.ptr] = self.memory[self.ptr] - 1 if self.memory[self.ptr] > 0 else 255
                
            elif code[i] == '.':    
                op.append(chr(self.memory[self.ptr]))

            elif code[i] == ',':
                self.memory[self.ptr] = (input()[0])

            elif code[i] == '[':
                if self.memory[self.ptr] == 0:
                    i = self.bracePos[i]

            elif code[i] == ']':
                if self.memory[self.ptr] != 0:
                    i = self.bracePos[i]
            i += 1
        return op
