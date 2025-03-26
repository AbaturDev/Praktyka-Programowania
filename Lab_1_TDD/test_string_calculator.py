from string_calculator import Add
import unittest


class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(Add(""), 0)

    def test_single_number(self):
        self.assertEqual(Add("1"), 1)
        self.assertEqual(Add("2"), 2)
        self.assertEqual(Add("5"), 5)

    def test_two_numbers(self):
        self.assertEqual(Add("1,2"), 3)
        self.assertEqual(Add("2,3"), 5)
        self.assertEqual(Add("5,5"), 10)

    def test_multiple_numbers(self):
        self.assertEqual(Add("1,2,3"), 6)
        self.assertEqual(Add("3,3,3"), 9)
        self.assertEqual(Add("5,20,30"), 55)

    def test_newline_separator(self):
        self.assertEqual(Add("1\n2,3"), 6)
        self.assertEqual(Add("1\n2\n3,5,5"), 16)

    def test_invalid_newline_placement(self):
        with self.assertRaises(ValueError):
            Add("1,\n")
        with self.assertRaises(ValueError):
            Add("1,2,-1,")
        with self.assertRaises(ValueError):
            Add("\n")
        with self.assertRaises(ValueError):
            Add(",")
        with self.assertRaises(ValueError):
            Add("1,\n,3,5\n8")
