"""
Unit tests for the calculator library
"""

import unittest
import calculator
 

class TestStringMethods(unittest.TestCase):


    def test_addition(self):
        a = 2
        b = 2 
        self.assertEqual(calculator.add(a, b), 4)

    def test_subtraction(self):
        c = 4
        d = 2
        self.assertEqual(calculator.subtract(c, d), 2)
    
    def test_multiplcation(self):
        e = 5
        f = 2
        self.assertEqual(calculator.multiply(e, f), 10)
    
    def test_divide(self):
        g = 5
        h = 2
        self.assertEqual(calculator.divide(g, h), 2)
