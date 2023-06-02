import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
from src.stsc_interpreter import Interpreter


class InterpreterTests(unittest.TestCase):
    def test1(self):
        instructions = []
        expected_output = ""
        interpreter = Interpreter(instructions)
        with redirect_stdout(StringIO()) as stdout:
            interpreter.run()
            actual_output = stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    def test2(self):
        instructions = ["3", "4", "print"]
        expected_output = "4.0"
        interpreter = Interpreter(instructions)
        with redirect_stdout(StringIO()) as stdout:
            interpreter.run()
            actual_output = stdout.getvalue().strip()

        self.assertEqual(actual_output, expected_output)

    def input_generator(self, inputs):
        for value in inputs:
            yield value

    def test3(self):
        instructions = ["uInput", "print"]
        expected_output = "2.5"
        user_inputs = ["2.5\n"]
        interpreter = Interpreter(instructions)
        with redirect_stdout(StringIO()) as stdout, \
                patch('builtins.input', lambda _: next(self.input_generator(user_inputs))):
            interpreter.run()
            actual_output = stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    def test4(self):
        instructions = ["uInput"]
        expected_output = "Invalid input. Please enter only numeric values."
        user_inputs = ["invalid\n"]
        interpreter = Interpreter(instructions)
        with redirect_stdout(StringIO()) as stdout, \
                patch('builtins.input', lambda _: next(self.input_generator(user_inputs))), \
                self.assertRaises(SystemExit):
            interpreter.run()
            actual_output = stdout.getvalue().strip()
            self.assertEqual(actual_output, expected_output)

    def test5(self):
        instructions = ["3", "4", "add", "print"]
        expected_output = "7.0"
        interpreter = Interpreter(instructions)
        with redirect_stdout(StringIO()) as stdout:
            interpreter.run()
            actual_output = stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

    def test6(self):
        instructions = ["10", "5", "sub", "print"]
        expected_output = "-5.0"
        interpreter = Interpreter(instructions)
        with redirect_stdout(StringIO()) as stdout:
            interpreter.run()
            actual_output = stdout.getvalue().strip()
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()