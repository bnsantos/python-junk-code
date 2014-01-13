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
from tests.trees.searchTreeTest import TestTrees
from tests.trees.binarySearchTreeTest import TestBinarySearchTrees
from tests.graphs.dijskstraTest import TestDijkstra
from tests.trees.binaryTreeTest import TestBinaryTrees
from tests.graphs.longSimplePathTest import TestLongSimplePath


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
    test_suite.addTest(unittest.makeSuite(TestMedian))
    test_suite.addTest(unittest.makeSuite(TestMostPopularName))
    test_suite.addTest(unittest.makeSuite(TestRank))
    test_suite.addTest(unittest.makeSuite(TestTopK))
    test_suite.addTest(unittest.makeSuite(TestMode))
    test_suite.addTest(unittest.makeSuite(TestStack))
    test_suite.addTest(unittest.makeSuite(TestLinkedList))
    test_suite.addTest(unittest.makeSuite(TestTrees))
    test_suite.addTest(unittest.makeSuite(TestBinarySearchTrees))
    test_suite.addTest(unittest.makeSuite(TestDijkstra))
    test_suite.addTest(unittest.makeSuite(TestBinaryTrees))
    test_suite.addTest(unittest.makeSuite(TestLongSimplePath))
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())