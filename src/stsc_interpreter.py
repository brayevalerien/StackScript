class Interpreter:
    def __init__(self, instructions: list[str]) -> None:
        self.stack = []
        self.instructions = instructions
        self.ip = 0 # instruction pointer
        
    def run(self):
        while self.ip != len(self.instructions):
            cur_instruction = self.instructions[self.ip]

            if cur_instruction.isnumeric():
                self.stack.append(float(cur_instruction))
            elif cur_instruction == "print":
                print(self.stack[-1])
            elif cur_instruction == "uInput":
                try:
                    self.stack.append(float(input("> ")))
                except:
                    print("Invalid input. Please enter only numeric values.")
                    exit(-1)
            elif cur_instruction == "add":
                # TODO check that there are at least two elements
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a + b)
            elif cur_instruction == "sub":
                # TODO check that there are at least two elements
                a, b = self.stack.pop(), self.stack.pop()
                self.stack.append(a - b)
            
            self.ip += 1