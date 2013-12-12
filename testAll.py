__author__ = 'bruno'
import unittest
from tests.validateInputTest import ValidateInputTest
from tests.factorialTest import TestFactorial
from tests.fibonacciTest import TestFibonacci
from tests.palindromeTest import PalindromeTest
from tests.bubbleSortTest import TestBubbleSort
from tests.insertionSortTest import TestInsertionSort
from tests.combSortTest import TestCombSort
from tests.gnomeSortTest import TestGnomeSort
from tests.cocktailSortTest import TestCocktailSort
from tests.oddEvenSortTest import TestOddEvenSort
from tests.linearSearchTest import TestLinearSort
from tests.peasantMultiplicationTest import TestPeasantMultiplication
from tests.leapYearTest import TestLeapYear
from tests.greatestCommonDivisor import TestGreatestCommonDivisor


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ValidateInputTest))
    test_suite.addTest(unittest.makeSuite(TestFactorial))
    test_suite.addTest(unittest.makeSuite(TestFibonacci))
    test_suite.addTest(unittest.makeSuite(PalindromeTest))
    test_suite.addTest(unittest.makeSuite(TestBubbleSort))
    test_suite.addTest(unittest.makeSuite(TestInsertionSort))
    test_suite.addTest(unittest.makeSuite(TestCombSort))
    test_suite.addTest(unittest.makeSuite(TestGnomeSort))
    test_suite.addTest(unittest.makeSuite(TestCocktailSort))
    test_suite.addTest(unittest.makeSuite(TestOddEvenSort))
    test_suite.addTest(unittest.makeSuite(TestLinearSort))
    test_suite.addTest(unittest.makeSuite(TestPeasantMultiplication))
    test_suite.addTest(unittest.makeSuite(TestLeapYear))
    test_suite.addTest(unittest.makeSuite(TestGreatestCommonDivisor))
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())