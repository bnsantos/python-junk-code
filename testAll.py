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
from tests.primeTest import TestPrimeNumber
from tests.numbersTest import TestNumberYear
from tests.abacusTest import TestAbacus
from tests.selectionSortTest import TestSelectionSort
from tests.selectionSearchTest import TestSelectionSearch
from tests.patienceSortTest import TestPatienceSort
from tests.quickSortTest import TestQuickSort
from tests.stoogeSortTest import TestStoogeSort
from tests.connectedComponentsTest import TestConnectedComponents
from tests.clusteringCoefficientTest import TestClusteringCoefficient
from tests.breadthFirstSearchTest import TestBreadthFirstSearch
from tests.knapsackTest import TestKnapsack
from tests.caesarTest import TestCaesar
from tests.maximumTest import TestMaximum
from tests.minimumTest import TestMinimum
from tests.midpointTest import TestMidpoint
from tests.meanTest import TestMean


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
    test_suite.addTest(unittest.makeSuite(TestPrimeNumber))
    test_suite.addTest(unittest.makeSuite(TestNumberYear))
    test_suite.addTest(unittest.makeSuite(TestAbacus))
    test_suite.addTest(unittest.makeSuite(TestSelectionSort))
    test_suite.addTest(unittest.makeSuite(TestSelectionSearch))
    test_suite.addTest(unittest.makeSuite(TestPatienceSort))
    test_suite.addTest(unittest.makeSuite(TestQuickSort))
    test_suite.addTest(unittest.makeSuite(TestStoogeSort))
    test_suite.addTest(unittest.makeSuite(TestConnectedComponents))
    test_suite.addTest(unittest.makeSuite(TestClusteringCoefficient))
    test_suite.addTest(unittest.makeSuite(TestBreadthFirstSearch))
    test_suite.addTest(unittest.makeSuite(TestKnapsack))
    test_suite.addTest(unittest.makeSuite(TestCaesar))
    test_suite.addTest(unittest.makeSuite(TestMaximum))
    test_suite.addTest(unittest.makeSuite(TestMinimum))
    test_suite.addTest(unittest.makeSuite(TestMidpoint))
    test_suite.addTest(unittest.makeSuite(TestMean))
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())