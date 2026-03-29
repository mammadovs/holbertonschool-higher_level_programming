#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_no_args(self):
        """Test the function with no arguments passed."""
        self.assertIsNone(max_integer())

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of mixed integers and floats."""
        ints_and_floats = [1.53, 15.5, -2, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string (which is a sequence of characters)."""
        string = "Python"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Apple", "Zebra", "Banana"]
        self.assertEqual(max_integer(strings), "Zebra")

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        negatives = [-1, -5, -10, -2]
        self.assertEqual(max_integer(negatives), -1)

if __name__ == '__main__':
    unittest.main()
