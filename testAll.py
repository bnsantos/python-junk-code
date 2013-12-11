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


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ValidateInputTest))
    suite.addTest(unittest.makeSuite(TestFactorial))
    suite.addTest(unittest.makeSuite(TestFibonacci))
    suite.addTest(unittest.makeSuite(PalindromeTest))
    suite.addTest(unittest.makeSuite(TestBubbleSort))
    suite.addTest(unittest.makeSuite(TestInsertionSort))
    suite.addTest(unittest.makeSuite(TestCombSort))
    suite.addTest(unittest.makeSuite(TestGnomeSort))
    suite.addTest(unittest.makeSuite(TestCocktailSort))
    suite.addTest(unittest.makeSuite(TestOddEvenSort))
    suite.addTest(unittest.makeSuite(TestLinearSort))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())