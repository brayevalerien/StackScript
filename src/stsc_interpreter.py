import re
from src.stsc_parser import Parser

class Interpreter:
    PUSH_INSTRUCTION = "push"
    PRINT_INSTRUCTION = "print"
    UINPUT_INSTRUCTION = "uInput"
    SHOW_INSTRUCTION = "show"
    ADD_INSTRUCTION = "add"
    SUB_INSTRUCTION = "sub"
    JUMP_INSTRUCTION = "jump"
    JUMPZERO_INSTRUCTION = "jumpZero"
    JUMPNOTZERO_INSTRUCTION = "jumpNotZero"

    def __init__(self, parser: Parser) -> None:
        self.stack = []
        self.instructions = parser.tokens
        self.ip = 0  # instruction pointer
        self.tags = {}
        
    def is_number(self, s: str) -> bool:
        return bool(re.match(r'^[-+]?(\d+(\.\d*)?|\.\d+)$', s))
    
    def stsc_push(self, value: float):
        self.stack.append(float(value))
    
    def stsc_print(self, s: str):
        print(s)
        
    def stsc_uinput(self):
        try:
            self.stack.append(float(input("> ")))
        except:
            print("Invalid input. Please enter only numeric values.")
            exit(-1)
    
    def stsc_show(self):
        print(str(self.stack))
    
    def stsc_add(self):
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
    
    def stsc_sub(self):
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
    
    def stsc_jump(self, tag):
        if tag in self.tags:
            self.ip = self.tags[tag]
        else:
            print("A previously defined tag must be on top of the stack when a jump instruction is executed. Current top of the stack: " + str(tag))
            exit(-1)
    
    def stsc_jump_zero(self, tag):
        if len(self.stack) < 1:
            print("Cannot jump, the stack has less than one element.")
            exit(-1)
        if tag in self.tags:
            if self.stack[-1] == 0:
                self.ip = self.tags[tag]
        else:
            print("A previously defined tag must be on top of the stack when a jumpZero instruction is executed. Current top of the stack: " + str(tag))
            exit(-1)
    
    def stsc_jump_not_zero(self, tag):
        if len(self.stack) < 1:
            print("Cannot jump, the stack has less than one element.")
            exit(-1)
        if tag in self.tags:
            if self.stack[-1] != 0:
                self.ip = self.tags[tag]
        else:
            print("A previously defined tag must be on top of the stack when a jumpNotZero instruction is executed. Current top of the stack: " + str(tag))
            exit(-1)
    
    def run(self):
        instruction_mapping = {
            self.PUSH_INSTRUCTION: self.stsc_push,
            self.PRINT_INSTRUCTION: self.stsc_print,
            self.UINPUT_INSTRUCTION: self.stsc_uinput,
            self.SHOW_INSTRUCTION: self.stsc_show,
            self.ADD_INSTRUCTION: self.stsc_add,
            self.SUB_INSTRUCTION: self.stsc_sub,
            self.JUMP_INSTRUCTION: self.stsc_jump,
            self.JUMPZERO_INSTRUCTION: self.stsc_jump_zero,
            self.JUMPNOTZERO_INSTRUCTION: self.stsc_jump_not_zero,
        }
        
        while self.ip != len(self.instructions):
            cur_instruction = self.instructions[self.ip]

            # Check if the current instruction is a number
            if self.is_number(cur_instruction):
                instruction_mapping[self.PUSH_INSTRUCTION](cur_instruction)
                
            # I/O instructions
            elif cur_instruction == self.PRINT_INSTRUCTION:
                if len(self.stack) < 1:
                    print("Cannot print, the stack is empty.")
                    exit(-1)
                if isinstance(self.stack[-1], float):
                    msg = str(self.stack[-1])
                else:
                    msg = self.stack[-1] + " (tag)"
                print(msg)
            elif cur_instruction == self.UINPUT_INSTRUCTION:
                instruction_mapping[self.UINPUT_INSTRUCTION]()
            elif cur_instruction == self.SHOW_INSTRUCTION:
                instruction_mapping[self.SHOW_INSTRUCTION]()
            
            # Arithmetic instructions
            elif cur_instruction == self.ADD_INSTRUCTION:
                instruction_mapping[self.ADD_INSTRUCTION]()
            elif cur_instruction == self.SUB_INSTRUCTION:
                instruction_mapping[self.SUB_INSTRUCTION]()
                
            # Tag and jump instructions
            elif len(cur_instruction) > 0 and cur_instruction[0] == ">":
                if len(cur_instruction) < 2:
                    print("tags must have at least one character.")
                    exit(-1)
                self.tags[cur_instruction[1:]] = self.ip  # stores the position of the tag
            elif cur_instruction in self.tags:
                self.stack.append(cur_instruction)
            elif cur_instruction == self.JUMP_INSTRUCTION:
                if len(self.stack) < 1:
                    print("Cannot jump, the stack has less than one element.")
                    exit(-1)
                stack_top = self.stack.pop()
                instruction_mapping[self.JUMP_INSTRUCTION](stack_top)
            elif cur_instruction == self.JUMPZERO_INSTRUCTION:
                if len(self.stack) < 1:
                    print("Cannot jump, the stack has less than one element.")
                    exit(-1)
                stack_top = self.stack.pop()
                instruction_mapping[self.JUMPZERO_INSTRUCTION](stack_top)
            elif cur_instruction == self.JUMPNOTZERO_INSTRUCTION:
                if len(self.stack) < 1:
                    print("Cannot jump, the stack has less than one element.")
                    exit(-1)
                stack_top = self.stack.pop()
                instruction_mapping[self.JUMPNOTZERO_INSTRUCTION](stack_top)
                    
            # Unrecognized instruction
            else:
                print("Unrecognized instruction: " + cur_instruction)
                exit(-1)
                
            self.ip += 1
# 