import sys
from stsc_parser import Parser
from stsc_interpreter import Interpreter


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No source file provided.")
        exit(-1)
        
    try:
        with open(sys.argv[1]) as f:
            raw_code = f.read()
    except FileNotFoundError:
        print("File " + sys.argv[1] + " not found.")
        exit(-1)
        
    code_parser = Parser()
    code_parser.parse(raw_code)
    
    Interpreter(code_parser).run()