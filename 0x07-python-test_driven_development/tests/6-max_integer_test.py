"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_basic(self):
        # Test a basic case where the max integer is in the middle
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_integer_empty_list(self):
        # Test an empty list
        self.assertIsNone(max_integer([]))

    def test_max_integer_negative_numbers(self):
        # Test a list with negative numbers
        self.assertEqual(max_integer([-5, -3, -10, -1]), -1)

    def test_max_integer_duplicate_numbers(self):
        # Test a list with duplicate numbers
        self.assertEqual(max_integer([10, 10, 10]), 10)

    def test_max_integer_single_element(self):
        # Test a list with a single element
        self.assertEqual(max_integer([100]), 100)

    def test_max_integer_large_numbers(self):
        # Test a list with large numbers
        self.assertEqual(max_integer([999999, 1000000, 999998]), 1000000)

    def test_max_integer_mixed_numbers(self):
        # Test a list with mixed positive and negative numbers
        self.assertEqual(max_integer([-10, 0, 10, -5]), 10)

if __name__ == '__main__':
    unittest.main()
