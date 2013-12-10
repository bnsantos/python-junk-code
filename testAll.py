__author__ = 'bruno'
import unittest
import sys
sys.path.insert(0, '/tests')
from tests.validateInputTest import ValidateInputTest
from tests.factorialTest import TestFactorial
from tests.fibonacciTest import TestFibonacci


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ValidateInputTest))
    suite.addTest(unittest.makeSuite(TestFactorial))
    suite.addTest(unittest.makeSuite(TestFibonacci))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())