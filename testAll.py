__author__ = 'bruno'
import unittest
from tests.rectangleOverlapTest import TestRectangleOverlap


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRectangleOverlap))

    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())