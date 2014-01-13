__author__ = 'bruno'
import unittest
import algorithms.graphs.longSimplePath as LongSimplePath


class TestLongSimplePath(unittest.TestCase):
    def setUp(self):
        pass

    def test_long_simple_path_1(self):
        graph = {1: {2: 1, 3: 1}, 2: {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}, 3: {1: 1, 2: 1, 6: 1}, 4: {2: 1, 5: 1},
                 5: {2: 1, 4: 1}, 6: {2: 1, 3: 1}}
        self.assertEqual(None,
                         LongSimplePath.long_and_simple_path(graph, 1, 4, 6))

    def test_long_simple_path_2(self):
        flights = [(1, 2), (1, 3), (2, 3), (2, 6), (2, 4), (2, 5), (3, 6), (4, 5)]
        graph = {}
        for (x, y) in flights:
            LongSimplePath.make_link(graph, x, y)
        self.assertEqual(False,
                         LongSimplePath.long_and_simple_path(graph, 1, 3, 6))
