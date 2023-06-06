import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
from src.stsc_interpreter import Interpreter
from src.stsc_parser import Parser


class InterpreterTests(unittest.TestCase):
    def run_interpreter_test(self, instructions, expected_output):
        parser = Parser()
        parser.parse(instructions)
        interpreter = Interpreter(parser)
        with redirect_stdout(StringIO()) as stdout:
            interpreter.run()
            actual_output = stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    def input_generator(self, inputs):
        for value in inputs:
            yield value

    def run_interpreter_test_with_input(self, instructions, expected_output, user_inputs):
        with patch('builtins.input', lambda _: next(self.input_generator(user_inputs))):
            self.run_interpreter_test(instructions, expected_output)

    def test1(self):
        instructions = ""
        expected_output = ""
        self.run_interpreter_test(instructions, expected_output)

    def test2(self):
        instructions = "3 4 print"
        expected_output = "4.0"
        self.run_interpreter_test(instructions, expected_output)

    def test3(self):
        instructions = "uInput print"
        expected_output = "2.5"
        user_inputs = ["2.5\n"]
        self.run_interpreter_test_with_input(instructions, expected_output, user_inputs)

    def test4(self):
        instructions = "uInput"
        expected_output = "Invalid input. Please enter only numeric values."
        user_inputs = ["invalid\n"]
        with self.assertRaises(SystemExit):
            self.run_interpreter_test_with_input(instructions, expected_output, user_inputs)

    def test5(self):
        instructions = "3 4 add print"
        expected_output = "7.0"
        self.run_interpreter_test(instructions, expected_output)

    def test6(self):
        instructions = "10 5 sub print"
        expected_output = "-5.0"
        self.run_interpreter_test(instructions, expected_output)

    def test7(self):
        instructions = "5 >loop -1 add loop jumpNotZero print"
        expected_output = "0"
        self.run_interpreter_test(instructions, expected_output)

    def test7(self):
        instructions = "5 >loop -1 add 0 jumpNotZero"
        expected_output = "A previously defined tag must be on top of the stack when a jumpNotZero instruction is executed. Current top of the stack: 0.0"
        with self.assertRaises(SystemExit):
            self.run_interpreter_test(instructions, expected_output)


if __name__ == '__main__':
    unittest.main()
