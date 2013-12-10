__author__ = 'bruno'
import unittest
import sys
sys.path.insert(0, '/tests')
from tests.factorialTest import TestFactorial


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFactorial))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())