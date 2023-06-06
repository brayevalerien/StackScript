from src.stsc_parser import Parser

class Interpreter:
    def __init__(self, parser: Parser) -> None:
        self.stack = []
        self.instructions = parser.tokens
        
        self.ip = 0 # instruction pointer
        self.tags = {}
        
    def is_number(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False
        
    def run(self):
        while self.ip != len(self.instructions):
            cur_instruction = self.instructions[self.ip]

            # number to push to the stack
            if self.is_number(cur_instruction):
                self.stack.append(float(cur_instruction))
                
            # I/O instructions
            elif cur_instruction == "print":
                if len(self.stack) < 1:
                    print("Cannot print, the stack is empty.")
                    exit(-1)
                if isinstance(self.stack[-1], float):
                    msg = str(self.stack[-1])
                else:
                    msg = self.stack[-1] + " (tag)"
                print(msg)
            elif cur_instruction == "uInput":
                try:
                    self.stack.append(float(input("> ")))
                except:
                    print("Invalid input. Please enter only numeric values.")
                    exit(-1)
            elif cur_instruction == "show":
                print(str(self.stack))
            
            # arithmetic instructions
            elif cur_instruction == "add":
                if len(self.stack) < 2:
                    print("Cannot add, the stack has less than one element.")
                    exit(-1)
                a, b = self.stack.pop(), self.stack.pop()
                if isinstance(a, str):
                    print("Cannot add " + a + " (tag) and " + b + ".")
                    exit(-1)
                if isinstance(b, str):
                    print("Cannot add " + a + " and " + b + " (tag).")
                    exit(-1)
                self.stack.append(a + b)
            elif cur_instruction == "sub":
                if len(self.stack) < 2:
                    print("Cannot add, the stack has less than one element.")
                    exit(-1)
                a, b = self.stack.pop(), self.stack.pop()
                if isinstance(a, str):
                    print("Cannot sub " + a + " (tag) and " + b + ".")
                    exit(-1)
                if isinstance(b, str):
                    print("Cannot sub " + a + " and " + b + " (tag).")
                    exit(-1)
                self.stack.append(a - b)
                
            # tag and jump instructions
            elif 0<len(cur_instruction) and cur_instruction[0]==">": # cur_instruction is a tag
                if (len(cur_instruction)<2):
                    print("tags must have at least one caracter.")
                    exit(-1)
                self.tags[cur_instruction[1:]] = self.ip # stores the position of the tag
            elif self.tags.__contains__(cur_instruction):
                self.stack.append(cur_instruction)
            elif cur_instruction == "jump":
                if len(self.stack) < 1:
                    print("Cannot jump, the stack has less than one element.")
                    exit(-1)
                stack_top = self.stack.pop()
                if self.tags.__contains__(stack_top):
                    self.ip = self.tags[stack_top]
                else:
                    print("A previously defined tag must be on top of the stack when a jump instruction is executed. Current top of the stack: " + str(stack_top))
                    exit(-1)
            elif cur_instruction == "jumpZero":
                if len(self.stack) < 1:
                    print("Cannot jump, the stack has less than one element.")
                    exit(-1)
                stack_top = self.stack.pop()
                if self.tags.__contains__(stack_top):
                    if self.stack[-1] == 0:
                        self.ip = self.tags[stack_top]
                else:
                    print("A previously defined tag must be on top of the stack when a jumpZero instruction is executed. Current top of the stack: " + str(stack_top))
                    exit(-1)
            elif cur_instruction == "jumpNotZero":
                if len(self.stack) < 1:
                    print("Cannot jump, the stack has less than one element.")
                    exit(-1)
                stack_top = self.stack.pop()
                if self.tags.__contains__(stack_top):
                    if self.stack[-1] != 0:
                        self.ip = self.tags[stack_top]
                else:
                    print("A previously defined tag must be on top of the stack when a jumpNotZero instruction is executed. Current top of the stack: " + str(stack_top))
                    exit(-1)
                    
            # unrecognized instruction
            else:
                print("Unrecognized instruction: " + cur_instruction)
                exit(-1)
            self.ip += 1