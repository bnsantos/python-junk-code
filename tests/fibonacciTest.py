__author__ = 'bruno'
import unittest
import sys
sys.path.insert(0, '../algorithms')
import algorithms.fibonacci as Fibonacci


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        pass

    def test_recursive_fibonacci1(self):
        self.assertEqual(0, Fibonacci.recursive(0))

    def test_recursive_fibonacci2(self):
        self.assertEqual(233, Fibonacci.recursive(13))

    def test_recursive_fibonacci3(self):
        self.assertEqual(6765, Fibonacci.recursive(20))

    def test_incremental_fibonacci1(self):
        self.assertEqual(0, Fibonacci.incremental(0))

    def test_incremental_fibonacci2(self):
        self.assertEqual(233, Fibonacci.incremental(13))

    def test_incremental_fibonacci3(self):
        self.assertEqual(6765, Fibonacci.incremental(20))

    def test_incremental_fibonacci4(self):
        self.assertEqual(13, Fibonacci.incremental(7))