__author__ = 'bruno'
import unittest
import algorithms.graphs.longSimplePath as LongSimplePath


class TestLongSimplePath(unittest.TestCase):
    def setUp(self):
        pass

    def test_long_simple_path_1(self):
        graph = {1: {2: 1, 3: 1}, 2: {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}, 3: {1: 1, 2: 1, 6: 1}, 4: {2: 1, 5: 1},
                 5: {2: 1, 4: 1}, 6: {2: 1, 3: 1}}
        self.assertEqual([1, 3, 6, 2, 5, 4],
                         LongSimplePath.long_and_simple_path(graph, 1, 4, 6))

    def test_long_simple_path_2(self):
        flights = [(1, 2), (1, 3), (2, 3), (2, 6), (2, 4), (2, 5), (3, 6), (4, 5)]
        graph = {}
        for (x, y) in flights:
            LongSimplePath.make_link(graph, x, y)
        self.assertEqual(False,
                         LongSimplePath.long_and_simple_path(graph, 1, 3, 6))

    def test_long_simple_path_3(self):
        flights = [(1, 2), (1, 3), (2, 3), (2, 6), (2, 4), (2, 5), (3, 6), (4, 5)]
        graph = {}
        for (x, y) in flights:
            LongSimplePath.make_link(graph, x, y)
        self.assertEqual([1, 3],
                         LongSimplePath.long_and_simple_path(graph, 1, 3, 1))

    def test_long_simple_path_4(self):
        graph = {1: {2: 1, 3: 1}, 2: {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}, 3: {1: 1, 2: 1, 6: 1}, 4: {2: 1, 5: 1},
                 5: {2: 1, 4: 1}, 6: {2: 1, 3: 1}}
        self.assertEqual([1, 2, 5],
                         LongSimplePath.long_and_simple_path(graph, 1, 5, 3))

    def test_long_simple_path_5(self):
        graph = {1: {2: 1, 3: 1}, 2: {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}, 3: {1: 1, 2: 1, 6: 1}, 4: {2: 1, 5: 1},
                 5: {2: 1, 4: 1}, 6: {2: 1, 3: 1}}
        self.assertEqual([1, 3, 6],
                         LongSimplePath.long_and_simple_path(graph, 1, 6, 3))

    def test_long_simple_path_6(self):
        graph = {1: {2: 1, 3: 1}, 2: {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}, 3: {1: 1, 2: 1, 6: 1}, 4: {2: 1, 5: 1},
                 5: {2: 1, 4: 1}, 6: {2: 1, 3: 1}}
        self.assertEqual([2, 4],
                         LongSimplePath.long_and_simple_path(graph, 2, 4, 1))

    def test_long_simple_path_7(self):
        graph = {1: {2: 1, 3: 1}, 2: {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}, 3: {1: 1, 2: 1, 6: 1}, 4: {2: 1, 5: 1},
                 5: {2: 1, 4: 1}, 6: {2: 1, 3: 1}}
        self.assertEqual([3, 6],
                         LongSimplePath.long_and_simple_path(graph, 3, 6, 1))

    def test_long_simple_path_8(self):
        graph = {1: {2: 1, 3: 1}, 2: {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}, 3: {1: 1, 2: 1, 6: 1}, 4: {2: 1, 5: 1},
                 5: {2: 1, 4: 1}, 6: {2: 1, 3: 1}}
        self.assertEqual([4, 2, 6, 3],
                         LongSimplePath.long_and_simple_path(graph, 4, 3, 2))

    def test_long_simple_path_9(self):
        graph = {1: {2: 1, 3: 1}, 2: {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}, 3: {1: 1, 2: 1, 6: 1}, 4: {2: 1, 5: 1},
                 5: {2: 1, 4: 1}, 6: {2: 1, 3: 1}}
        self.assertEqual([6, 3],
                         LongSimplePath.long_and_simple_path(graph, 6, 3, 1))

    def test_long_simple_path_10(self):
        graph = {1: {2: 1, 3: 1}, 2: {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}, 3: {1: 1, 2: 1, 6: 1}, 4: {2: 1, 5: 1},
                 5: {2: 1, 4: 1}, 6: {2: 1, 3: 1}}
        self.assertEqual([6, 2, 4],
                         LongSimplePath.long_and_simple_path(graph, 6, 4, 2))