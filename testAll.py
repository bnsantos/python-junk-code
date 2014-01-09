__author__ = 'bruno'
import unittest
from tests.helper.validateInputTest import ValidateInputTest
from tests.math.factorialTest import TestFactorial
from tests.math.fibonacciTest import TestFibonacci
from tests.string.palindromeTest import PalindromeTest
from tests.sort.bubbleSortTest import TestBubbleSort
from tests.sort.insertionSortTest import TestInsertionSort
from tests.sort.combSortTest import TestCombSort
from tests.sort.gnomeSortTest import TestGnomeSort
from tests.sort.cocktailSortTest import TestCocktailSort
from tests.sort.oddEvenSortTest import TestOddEvenSort
from tests.search.linearSearchTest import TestLinearSort
from tests.peasantMultiplicationTest import TestPeasantMultiplication
from tests.leapYearTest import TestLeapYear
from tests.math.greatestCommonDivisor import TestGreatestCommonDivisor
from tests.math.primeTest import TestPrimeNumber
from tests.math.numbersTest import TestNumberYear
from tests.math.abacusTest import TestAbacus
from tests.sort.selectionSortTest import TestSelectionSort
from tests.search.selectionSearchTest import TestSelectionSearch
from tests.sort.patienceSortTest import TestPatienceSort
from tests.sort.quickSortTest import TestQuickSort
from tests.sort.stoogeSortTest import TestStoogeSort
from tests.graphs.connectedComponentsTest import TestConnectedComponents
from tests.graphs.clusteringCoefficientTest import TestClusteringCoefficient
from tests.graphs.breadthFirstSearchTest import TestBreadthFirstSearch
from tests.knapsackTest import TestKnapsack
from tests.cripto.caesarTest import TestCaesar
from tests.statistics.maximumTest import TestMaximum
from tests.statistics.minimumTest import TestMinimum
from tests.statistics.midpointTest import TestMidpoint
from tests.statistics.meanTest import TestMean
from tests.statistics.medianTest import TestMedian
from tests.mostPopularName import TestMostPopularName
from tests.statistics.rankTest import TestRank
from tests.statistics.topKTest import TestTopK
from tests.statistics.modeTest import TestMode
from tests.lists.stackTest import TestStack
from tests.lists.linkedListTest import TestLinkedList
from tests.trees.treesTest import TestTrees


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTrees))
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())