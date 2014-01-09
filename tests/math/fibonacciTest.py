__author__ = 'bruno'
import unittest
import algorithms.math.fibonacci as Fibonacci


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        pass

    def test_recursive_fibonacci1(self):
        self.assertEqual(0, Fibonacci.recursive(0))

    def test_recursive_fibonacci2(self):
        self.assertEqual(233, Fibonacci.recursive(13))

    def test_recursive_fibonacci3(self):
        self.assertEqual(6765, Fibonacci.recursive(20))

    def test_recursive_fibonacci4(self):
        self.assertEqual(4181, Fibonacci.recursive(19))

    def test_recursive_fibonacci5(self):
        self.assertEqual(28657, Fibonacci.recursive(23))

    def test_incremental_fibonacci1(self):
        self.assertEqual(0, Fibonacci.incremental(0))

    def test_incremental_fibonacci2(self):
        self.assertEqual(233, Fibonacci.incremental(13))

    def test_incremental_fibonacci3(self):
        self.assertEqual(6765, Fibonacci.incremental(20))

    def test_incremental_fibonacci4(self):
        self.assertEqual(1548008755920, Fibonacci.incremental(60))

    def test_incremental_fibonacci5(self):
        self.assertEqual(433494437, Fibonacci.incremental(43))