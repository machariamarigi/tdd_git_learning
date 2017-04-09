"""This module will be used to test the functionality of our calculator
    application
"""

import unittest


class TestCalculator(unittest.TestCase):
    """Class contains several testcases for our application using Python's
        unittest module
    """

    def setUp(self):
        """Function sets up hooks up our calculator to variable calc"""
        self.calc = Caluculator()

    def test_calculator_add_works(self):
        """Funtion test if our function works"""
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

if __name__ == '__main__':
    unittest.main()
