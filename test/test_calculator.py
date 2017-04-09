"""This module will be used to test the functionality of our calculator
    application
"""

import unittest
from app.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Class contains several testcases for our application using Python's
        unittest module
    """

    def setUp(self):
        """Function sets up hooks up our calculator to variable calc"""
        self.calc = Calculator()

    def test_calculator_add_works(self):
        """test if our add function works"""
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_add_not_numbers(self):
        """Test to see if our add function adds only numbers"""
        self.assertRaises(ValueError, self.calc.add, "mash", "cool")

    def test_calculator_add_not_numbers_val1(self):
        """Test to see if our add function adds only numbers"""
        self.assertRaises(ValueError, self.calc.add, "mash", 1)

    def test_calculator_add_not_numbers_val2(self):
        """Test to see if our add function adds only numbers"""
        self.assertRaises(ValueError, self.calc.add, 2, "cool")

if __name__ == '__main__':
    unittest.main()
