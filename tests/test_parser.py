import unittest
from src.stsc_parser import Parser

class ParserTests(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.parser = Parser()

    def test1(self):
        test_sequence = ""
        expected_output = []
        actual_output = self.parser.parse(test_sequence)
        self.assertEqual(actual_output, expected_output)

    def test2(self):
        test_sequence = "1 2"
        expected_output = ["1", "2"]
        actual_output = self.parser.parse(test_sequence)
        self.assertEqual(actual_output, expected_output)

    def test3(self):
        test_sequence = "1 2 add"
        expected_output = ["1", "2", "add"]
        actual_output = self.parser.parse(test_sequence)
        self.assertEqual(actual_output, expected_output)

    def test4(self):
        test_sequence = "1 2 add\nprint"
        expected_output = ["1", "2", "add", "print"]
        actual_output = self.parser.parse(test_sequence)
        self.assertEqual(actual_output, expected_output)

    def test5(self):
        test_sequence = "1 2 add\n\tprint"
        expected_output = ["1", "2", "add", "print"]
        actual_output = self.parser.parse(test_sequence)
        self.assertEqual(actual_output, expected_output)

    def test6(self):
        test_sequence = "// full line comment\n1 2 add // this is a comment\nprint // another comment"
        expected_output = ["1", "2", "add", "print"]
        actual_output = self.parser.parse(test_sequence)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()