__author__ = 'bruno'
import unittest
from tests.validateInputTest import ValidateInputTest
from tests.factorialTest import TestFactorial
from tests.fibonacciTest import TestFibonacci
from tests.palindromeTest import PalindromeTest
from tests.bubbleSortTest import TestBubbleSort


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ValidateInputTest))
    suite.addTest(unittest.makeSuite(TestFactorial))
    suite.addTest(unittest.makeSuite(TestFibonacci))
    suite.addTest(unittest.makeSuite(PalindromeTest))
    suite.addTest(unittest.makeSuite(TestBubbleSort))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())