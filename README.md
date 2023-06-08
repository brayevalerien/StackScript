# StackScript
StackScript is a toy programming language, designed as a personal project to explore stack-based paradigm. This repository contains documentation about the language, a simple StackScript interpreter written in Python. While the language itself is not intended for real world use due to its limitations and inefficiency, it is a great learning tool and provides fun challenges when writing a program using it.<br>

Please note that this language and the provided interpreter are not intended for production use and should be treated purely as an educational and recreational tool. I cannot be held accountable for any mistakes it could lead to.<br>

This document is divided in multiple sections:
1. How to install and run StackScript programs
2. Core concepts
3. Instruction set
    1. I/O instructions
    2. Arithmetic instructions
    3. Jump Instructions
    4. Stack manipulation instructions
4. Code examples
5. How to contribute to the project

## How to install and run StackScript programs
Clone this repository locally using the command: <br>
`git clone https://github.com/brayevalerien/StackScript`

Once you have local version installed, run the [./src/stackscript.py](./src/stackscript.py) python script and pass the program file path in argument. For instance, if you want to run the [Fibonacci example](./examples/fibonacci.stsc), run the command:<br>
`python ./src/stackscript.py ./examples/fibonacci.stsc`

Note that python is required to run StackScript programs. 

## Core concepts


## Instruction set

### I/O instructions
- there is no push instruction. Simply write the number of the tag you want to push on the stack (e.g. `1 2 tag show` will output `[1.0, 2.0, 'tag']`)
- `print`
- `uInput`
- `show`

### Arithmetic instructions
- `add`
- `sub`
- `mul`
- `div`

### Jump instructions
- `>[tagName]` will register a tag named `tagName`
- `jump`
- `jumpZero`
- `jumpNotZero`

### Stack manipulation instructions
- `dup`
- `swap`
- `reach`
- `cycle`


## Code examples
All code examples are available at [./examples/](./examples/) for you to run them.

## How to contribute to the project