![StackScript logo](./logo/stackscript_logo_cropped.png)
# StackScript
StackScript is a toy programming language, designed as a personal project to explore stack-based paradigm. This repository contains documentation about the language and a simple StackScript interpreter written in Python. While the language itself is not intended for real world use due to its limitations and inefficiency, it is a great learning tool and provides fun challenges when writing a program using it.<br>

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
    1. arithmetic.stsc
    2. loop.stsc
    3. fibonacci.stsc
5. How to contribute to the project
    1. How to add an instruction
    2. Things you could help with

## How to install and run StackScript programs
Clone this repository locally using the command: <br>
`git clone https://github.com/brayevalerien/StackScript`

Add the path of the directory to your `PYTHONPATH` environnement variable. You can `cd` into the directory you downloaded and run `export PYTHONPATH=$PYTHONPATH:${pwd}`.

Once you have local version installed, run the [./src/stackscript.py](./src/stackscript.py) python script and pass the program file path in argument. For instance, if you want to run the [Fibonacci example](./examples/fibonacci.stsc), run the command:<br>
`python ./src/stackscript.py ./examples/fibonacci.stsc`

Note that python is required to run StackScript programs. 

## Core concepts
StackScript relies heavily on the concept of a stack. A stack is a data structure that is similar to a list, as it stores elements at memory addresses. However, a stack differs from a list in that it only allows the user to interact with the top element. This means that to operate on an element at the bottom of the stack, the user must first remove (pop) all elements above it. Similarly, elements can only be added to the top of the stack through a process called pushing.<br>
In StackScript, the stack can only store two types of elements:
- Floating-point numbers
- Tags, which are objects that point to instructions in the source code.

As a result, StackScript does not have native support for characters, strings, or more complex data structures like arrays. Moreover, there is no way to define variables or procedures/functions.<br>
A StackScript program consists of instructions, which can be separated from each other by spaces, tabs, and/or line breaks. These instructions are executed one by one by the interpreter, performing the corresponding operations. To get a better idea of how this works all together, see the examples section.

## Instruction set
### I/O instructions
- `print`: prints the top of the stack to the standard output.
- `uInput`: reads a value from the standard input. Values that are not convertible to float are invalid.
- `show`: prints the whole stack to the standard output formatted as `[elem1, elem2, ... elemn]` where `elemn` is the top of the stack and `elem1` the bottom of the stack.

### Arithmetic instructions
In this section, we will note a the second-to-top element and b the top element of the stack.
- `add`: pops a and b and pushes a+b
- `sub`: pops a and b and pushes b-a
- `mul`: pops a and b and pushes a*b
- `div`: pops a and b and pushes b/a

### Jump instructions
Tags are a used by jump instructions. A jump instruction (conditional or not) requires a registered tag to be on top of the stack when it is executed, and will jump to the position in the source code where the tag was registered. Note that jump instructions pop the tag that are on top of the stack when executed.
- `>tagName`: registers a tag named `tagName`.
- `jump`: unconditionally jumps to the tag that is currently on top of the stack
- `jumpZero`: jumps to the tag that is currently on top of the stack iff the second-to-top element is 0.
- `jumpNotZero`: jumps to the tag that is currently on top of the stack iff the second-to-top element is not 0.
- `jumpPos`: jumps to the tag that is currently on top of the stack iff the second-to-top element is greater than or equal to 0.
- `jumpNeg`: jumps to the tag that is currently on top of the stack iff the second-to-top element is strictly less than 0.

### Stack manipulation instructions
- there is no push instruction. Simply write the number or the tag you want to push on the stack (e.g. `1 2 tag show` will output `[1.0, 2.0, 'tag']`)
- `dup`: duplicates the top element and pushes it on the top of the stack (e.g. `1 dup show` will output `[1.0, 1.0]`).
- `drop`: pops the top element and discards it.
- `swap`: swaps the top two elements of the stack.
- `reach`: similar to `dup`, but it duplicates the second-to-top element.
- `cycle`: cycles the top three elements, bringing the one at the bottom on top.
- `clear`: removes all elements from the stack

## Code examples
All code examples are available at [./examples/](./examples/) for you to run them. Some of them are explained in this section.

### [arithmetic.stsc](./examples/arithmetic.stsc)
This simple program demonstrates the use of the stack to compute simple math expression, how to display the result and use the `drop` instruction.
```
27 42 add print drop
27 42 sub print drop
27 42 mul print drop
27 42 div print drop
```
Each line starts by pushing the numbers 27 and 42 on top of the stack. Then it uses one of the four arithmetic instruction to add, substract, multiply and divide the numbers that were added to the stack, then prints the top of the stack (the result of the math operation) and finally dops the top element (cleaning the stack). The expected output is:
```c
69.0               // 42+27
15.0               // 42-27
1134.0             // 42*27
1.5555555555555556 // 42/27
```

### [loop.stsc](./examples/loop.stsc)
This example shows a simple way to make a for loop using tags and conditional jump instructions.
```
10 print
>loop -1 add
    print
loop jumpNotZero
```
The first line pushes 10 on top of the stack and prints it. A tag named "loop" is defined in the second line and we start the loop by decrementing the value on top of the stack (decrementing the value on top of the stack is done by `-1 add`). The value is then printed. The last line will jump the the `loop` tag iff the value on top of the stack is different from 0. The expected output of this program is:
```c
10.0
9.0
8.0
7.0
6.0
5.0
4.0
3.0
2.0
1.0
0.0
```
Note that this program is equivalent and very similar to the following C code
```c
    double i;
    for (i = 10.0; i != 0.0; i--) {
        printf("%f\n", i);
    }
```
Both codes have a simple way to express:
- a way to initialize the loop counter
- a condition for the loop to be executed again
- some code to execute at the end of a loop

### [fibonacci.stsc](./examples/fibonacci.stsc)
this program is a bit more complex but it computes the first terms of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence). It uses many important concepts of StackScript, including stack manipulation.
```
1 print 1 print
20
>nextTerm
    -1 add
    cycle cycle
    swap reach add
    print
    cycle
nextTerm jumpNotZero
```
The first line initializes the program by putting the first two terms of the Fibonacci sequence on top of the stack (1 and 1). It defines the number of terms to compute at line 2(in addition to the first two terms). Then, it uses a loop that computes and prints the next term. The `-1 add` instruction decrements the term counter and `cycle cycle` puts the counter at the bottom of the stack and bring the previous two terms of the sequence on top. `swap reach add` adds the two terms on top but makes sure that in the end, the bottom-most of the two is the n-2 term (for instance, if `[a, b]` is the top of the stack, after this line the top of the stack will be `[b, a+b]`). We then print the result and bring the counter to the top of the stack using `cycle`. This is repeated until the counter is equal to 0.

## How to contribute to the project

You can open issues and pull requests at any time, I check Github daily. If you took some time to contribute to the project, thank you very much.

### How to add an instruction
If you have an idea for an interesting (or necessary) instruction to be added to the interpreter, it is pretty simple since the interpreter is written to make adding instructions easy.

You only need to modify [stsc_interpreter.py](./src/stsc_interpreter.py), please follow these steps:
1. At the top of the `Interpreter` class, define a new constant `<INST_NAME>_INSTRUCTION` with the name of the instruction.
2. Define a function above `Interpreter.run`, called `stsc_<inst_name>`, that does what your instruction is supposed to do. This function can take arguments and manipulate the stack, `self.stack` as well as the registered tags stored in `self.tags`
3. In the `Interpreter.run` function, add an entry to the `instruction_mapping`: the key should be the constant you defined at step 1. and the value should be the function you defined at step 2.
4. In the same `run` function, add an `elif` case corresponding to your instruction.

Keep in mind that StackScript is made to be extremely basic and limited, so I might not accept pull request of instructions that add more complexity to the language or that do not fit the idea of it.

### Things you could help with
Here are some ideas of what you could work on if you want to contribute to the project but don't know where to start. They should be fairly simple to do but would make great contributions:
- create a C program to add a better way to run the interpreter. At the moment running a stsc program is a by awkward: `python ./src/stackscript.py path_to_program`. It would be easier if an exe file handled the call to python, so the user could simply run `./stackscript path_to_program`
- either prove that StackScript is Turing complete or that it is not. Even if it is not Turing complete, it would be great to know.
- improve the documentation by adding better examples, correcting grammar mistakes/typos and make the explanations clearer.