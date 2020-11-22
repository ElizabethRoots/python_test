"""
Unit tests for the calculator library
"""

import unittest
import calculator
 

class TestStringMethods(unittest.TestCase):


    def test_addition(self):
        a = 2
        b = 2 
        assert 4 == calculator.add(a, b) 
        self.assertEqual(calculator.add(a, b), 4)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

if __name__ == "__main__":
    unittest.main()
