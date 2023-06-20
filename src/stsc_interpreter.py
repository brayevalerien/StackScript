import re
from src.stsc_parser import Parser

class Interpreter:
    # push instruction
    PUSH_INSTRUCTION = "push"
    # I/O instructions
    PRINT_INSTRUCTION = "print"
    UINPUT_INSTRUCTION = "uInput"
    SHOW_INSTRUCTION = "show"
    # arithmetic insructions
    ADD_INSTRUCTION = "add"
    SUB_INSTRUCTION = "sub"
    MUL_INSTRUCTION = "mul"
    DIV_INSTRUCTION = "div"
    # jump instructions
    JUMP_INSTRUCTION = "jump"
    JUMPZERO_INSTRUCTION = "jumpZero"
    JUMPNOTZERO_INSTRUCTION = "jumpNotZero"
    JUMPPOS_INSTRUCTION = "jumpPos"
    JUMPNEG_INSTRUCTION = "jumpNeg"
    # stack manipulation instructions
    DUP_INSTRUCTION = "dup"    # (a -- a a)
    SWAP_INSTRUCTION = "swap"  # (a b -- b a)
    DROP_INSTRUCTION = "drop"   # (a -- )
    REACH_INSTRUCTION = "reach"  # (a b -- a b a)
    CYCLE_INSTRUCTION = "cycle"  # (a b c -- b c a)
    CLEAR_INSTRUCTION = "clear"  # (a b c -- )

    def __init__(self, parser: Parser) -> None:
        self.stack = []
        self.instructions = parser.tokens
        self.ip = 0  # instruction pointer
        self.tags = parser.tags
        
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
            exit(1)
    
    def stsc_show(self):
        print(str(self.stack))
    
    def stsc_add(self):
        if len(self.stack) < 2:
            print("Cannot add, the stack has less than two elements.")
            exit(1)
        a, b = self.stack.pop(), self.stack.pop()
        if isinstance(a, str):
            print("Cannot add " + a + " (tag) and " + b + ".")
            exit(1)
        if isinstance(b, str):
            print("Cannot add " + a + " and " + b + " (tag).")
            exit(1)
        self.stack.append(a + b)
    
    def stsc_sub(self):
        if len(self.stack) < 2:
            print("Cannot add, the stack has less than two elements.")
            exit(1)
        a, b = self.stack.pop(), self.stack.pop()
        if isinstance(a, str):
            print("Cannot sub " + a + " (tag) and " + b + ".")
            exit(1)
        if isinstance(b, str):
            print("Cannot sub " + a + " and " + b + " (tag).")
            exit(1)
        self.stack.append(a - b)
    
    def stsc_mul(self):
        if len(self.stack) < 2:
            print("Cannot mul, the stack has less than two elements.")
            exit(1)
        a, b = self.stack.pop(), self.stack.pop()
        if isinstance(a, str):
            print("Cannot mul " + a + " (tag) and " + b + ".")
            exit(1)
        if isinstance(b, str):
            print("Cannot mul " + a + " and " + b + " (tag).")
            exit(1)
        self.stack.append(a * b)
    
    def stsc_div(self):
        if len(self.stack) < 2:
            print("Cannot div, the stack has less than two elements.")
            exit(1)
        a, b = self.stack.pop(), self.stack.pop()
        if isinstance(a, str):
            print("Cannot div " + a + " (tag) and " + b + ".")
            exit(1)
        if isinstance(b, str):
            print("Cannot div " + a + " and " + b + " (tag).")
            exit(1)
        if b == 0:
            print("Cannot div by 0.")
            exit(1)
        self.stack.append(a / b)
    
    def stsc_jump(self, tag):
        if tag in self.tags:
            self.ip = self.tags[tag]
        else:
            print("A previously defined tag must be on top of the stack when a jump instruction is executed. Current top of the stack: " + str(tag))
            exit(1)
    
    def stsc_jump_zero(self, tag):
        if len(self.stack) < 1:
            print("Cannot jump, the stack has less than one element.")
            exit(1)
        if tag in self.tags:
            if self.stack[-1] == 0:
                self.ip = self.tags[tag]
        else:
            print("A previously defined tag must be on top of the stack when a jumpZero instruction is executed. Current top of the stack: " + str(tag))
            exit(1)
    
    def stsc_jump_not_zero(self, tag):
        if len(self.stack) < 1:
            print("Cannot jump, the stack has less than one element.")
            exit(1)
        if tag in self.tags:
            if self.stack[-1] != 0:
                self.ip = self.tags[tag]
        else:
            print("A previously defined tag must be on top of the stack when a jumpNotZero instruction is executed. Current top of the stack: " + str(tag))
            exit(1)
    
    def stsc_jump_pos(self, tag):
        if len(self.stack) < 1:
            print("Cannot jump, the stack has less than one element.")
            exit(1)
        if tag in self.tags:
            if self.stack[-1] >= 0:
                self.ip = self.tags[tag]
        else:
            print("A previously defined tag must be on top of the stack when a jumpPos instruction is executed. Current top of the stack: " + str(tag))
            exit(1)
    
    def stsc_jump_neg(self, tag):
        if len(self.stack) < 1:
            print("Cannot jump, the stack has less than one element.")
            exit(1)
        if tag in self.tags:
            if self.stack[-1] < 0:
                self.ip = self.tags[tag]
        else:
            print("A previously defined tag must be on top of the stack when a jumpNeg instruction is executed. Current top of the stack: " + str(tag))
            exit(1)
    
    def stsc_dup(self):
        if len(self.stack) < 1:
            print("Cannot dup, the stack has less than one element.")
            exit(1)
        self.stack.append(self.stack[-1])            
    
    def stsc_swap(self):
        if len(self.stack) < 2:
            print("Cannot swap, the stack has less than two elements.")
            exit(1)
        a, b = self.stack.pop(), self.stack.pop()
        self.stack.append(a)
        self.stack.append(b)
    
    def stsc_drop(self):
        if len(self.stack) < 1:
            print("Cannot drop, the stack has less than one element.")
            exit(1)
        self.stack.pop()            

    def stsc_reach(self):
        if len(self.stack) < 2:
            print("Cannot reach, the stack has less than two elements.")
            exit(1)
        self.stack.append(self.stack[-2])    

    def stsc_cycle(self):
        if len(self.stack) < 3:
            print("Cannot cycle, the stack has less than three elements.")
            exit(1)
        c, b, a = self.stack.pop(), self.stack.pop(), self.stack.pop()
        self.stack.append(b)
        self.stack.append(c)
        self.stack.append(a)

    def stsc_clear(self):
        self.stack.clear()
    
    def run(self):
        instruction_mapping = {
            # push instruction
            self.PUSH_INSTRUCTION: self.stsc_push,
            # I/O instructions
            self.PRINT_INSTRUCTION: self.stsc_print,
            self.UINPUT_INSTRUCTION: self.stsc_uinput,
            self.SHOW_INSTRUCTION: self.stsc_show,
            # arithmetic insructions
            self.ADD_INSTRUCTION: self.stsc_add,
            self.SUB_INSTRUCTION: self.stsc_sub,
            self.MUL_INSTRUCTION: self.stsc_mul,
            self.DIV_INSTRUCTION: self.stsc_div,
            # jump instructions
            self.JUMP_INSTRUCTION: self.stsc_jump,
            self.JUMPZERO_INSTRUCTION: self.stsc_jump_zero,
            self.JUMPNOTZERO_INSTRUCTION: self.stsc_jump_not_zero,
            self.JUMPPOS_INSTRUCTION: self.stsc_jump_pos,
            self.JUMPNEG_INSTRUCTION: self.stsc_jump_neg,
            # stack manipulation instructions
            self.DUP_INSTRUCTION: self.stsc_dup,
            self.SWAP_INSTRUCTION: self.stsc_swap,
            self.DROP_INSTRUCTION: self.stsc_drop,
            self.REACH_INSTRUCTION: self.stsc_reach,
            self.CYCLE_INSTRUCTION: self.stsc_cycle,
            self.CLEAR_INSTRUCTION: self.stsc_clear
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
                    exit(1)
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
            elif cur_instruction == self.MUL_INSTRUCTION:
                instruction_mapping[self.MUL_INSTRUCTION]()
            elif cur_instruction == self.DIV_INSTRUCTION:
                instruction_mapping[self.DIV_INSTRUCTION]()
                
            # Tag and jump instructions
            elif len(cur_instruction) > 0 and cur_instruction[0] == ">":
                pass # tags are already registered in stsc_parcer.py
            elif cur_instruction in self.tags:
                self.stack.append(cur_instruction)
            elif cur_instruction == self.JUMP_INSTRUCTION:
                stack_top = self.stack.pop()
                instruction_mapping[self.JUMP_INSTRUCTION](stack_top)
            elif cur_instruction == self.JUMPZERO_INSTRUCTION:
                stack_top = self.stack.pop()
                instruction_mapping[self.JUMPZERO_INSTRUCTION](stack_top)
            elif cur_instruction == self.JUMPNOTZERO_INSTRUCTION:
                stack_top = self.stack.pop()
                instruction_mapping[self.JUMPNOTZERO_INSTRUCTION](stack_top)
            elif cur_instruction == self.JUMPPOS_INSTRUCTION:
                stack_top = self.stack.pop()
                instruction_mapping[self.JUMPPOS_INSTRUCTION](stack_top)
            elif cur_instruction == self.JUMPNEG_INSTRUCTION:
                stack_top = self.stack.pop()
                instruction_mapping[self.JUMPNEG_INSTRUCTION](stack_top)

            # stack operation instructions
            elif cur_instruction == self.DUP_INSTRUCTION:
                instruction_mapping[self.DUP_INSTRUCTION]()
            elif cur_instruction == self.SWAP_INSTRUCTION:
                instruction_mapping[self.SWAP_INSTRUCTION]()
            elif cur_instruction == self.DROP_INSTRUCTION:
                instruction_mapping[self.DROP_INSTRUCTION]()
            elif cur_instruction == self.REACH_INSTRUCTION:
                instruction_mapping[self.REACH_INSTRUCTION]()
            elif cur_instruction == self.CYCLE_INSTRUCTION:
                instruction_mapping[self.CYCLE_INSTRUCTION]()
            elif cur_instruction == self.CLEAR_INSTRUCTION:
                instruction_mapping[self.CLEAR_INSTRUCTION]()
                    
            # Unrecognized instruction
            else:
                print("Unrecognized instruction: " + cur_instruction)
                exit(1)
                
            self.ip += 1