# https://github.com/nakalobiusUFL/lab10-NK-LS.git
# Partner 1: Natalie Kalobius
# Partner 2: Lana Salvador

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(1, 6), 7)
        self.assertEqual(add(5, 5), 10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(subtract(10, 2), 8)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 5), 10)
        self.assertEqual(mul(-1, 3), -3)
        self.assertEqual(mul(6, 4), 24)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 10), 2)
        self.assertEqual(div(3, 0), 0)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        with self.assertRaises(ValueError):
            logarithm(4, -2)
            logarithm(-2, 4)
            logarithm(5, 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-10, 1)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
                logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(4, 3), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-2)

        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(100), 10)

# Do not touch this
if __name__ == "__main__":
    unittest.main()