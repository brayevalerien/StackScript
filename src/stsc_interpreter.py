from stsc_parser import Parser

class Interpreter:
    def __init__(self, parser: Parser) -> None:
        self.stack = []
        self.instructions = parser.tokens
        
        self.ip = 0 # instruction pointer
        self.flags = {}
        
    def is_number(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False
        
    def run(self):
        while self.ip != len(self.instructions):
            cur_instruction = self.instructions[self.ip]

            if self.is_number(cur_instruction):
                self.stack.append(float(cur_instruction))
            elif cur_instruction == "print":
                print(self.stack[-1])
            elif cur_instruction == "uInput":
                try:
                    self.stack.append(float(input("> ")))
                except:
                    print("Invalid input. Please enter only numeric values.")
                    exit(-1)
            elif cur_instruction == "trace":
                print(str(self.stack))
            elif cur_instruction == "add":
                # TODO check that there are at least two elements
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a + b)
            elif cur_instruction == "sub":
                # TODO check that there are at least two elements
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a - b)
            elif 0<len(cur_instruction) and cur_instruction[0]==">": # cur_instruction is a flag
                #TODO handle flags
                if (len(cur_instruction)<2):
                    print("Flags must have at least one caracter.")
                    exit(-1)
                self.flags[cur_instruction[1:]] = self.ip # stores the position of the flag
            elif self.flags.__contains__(cur_instruction):
                self.stack.append(cur_instruction)
            elif cur_instruction == "jump":
                stack_top = self.stack.pop()
                if self.flags.__contains__(stack_top):
                    self.ip = self.flags[stack_top]
                else:
                    print("A previously defined flag must be on top of the stack when a jump instruction is executed. Current top of the stack: " + str(stack_top))
                    exit(-1)
            elif cur_instruction == "jumpZero":
                stack_top = self.stack.pop()
                if self.flags.__contains__(stack_top):
                    if self.stack[-1] == 0:
                        self.ip = self.flags[stack_top]
                else:
                    print("A previously defined flag must be on top of the stack when a jumpZero instruction is executed. Current top of the stack: " + str(stack_top))
                    exit(-1)
            elif cur_instruction == "jumpNotZero":
                stack_top = self.stack.pop()
                if self.flags.__contains__(stack_top):
                    if self.stack[-1] != 0:
                        self.ip = self.flags[stack_top]
                else:
                    print("A previously defined flag must be on top of the stack when a jumpNotZero instruction is executed. Current top of the stack: " + str(stack_top))
                    exit(-1)
            else:
                print("Unrecognized instruction: " + cur_instruction)
                exit(-1)
            self.ip += 1