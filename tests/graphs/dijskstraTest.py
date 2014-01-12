__author__ = 'bruno'
import unittest
import algorithms.graphs.dijkstra as Dijkstra


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        pass

    def test_dijkstra1(self):
        graph = {'a': {'b': 1, 'c': 3},
                 'b': {'c': 1, 'd': 8},
                 'c': {'d': 1},
                 'd': {}}
        self.assertEqual(({'a': 0, 'b': 1, 'c': 2, 'd': 3}, {'c': 'b', 'b': 'a', 'd': 'c'}),
                         Dijkstra.dijkstra(graph, 'a', 'd'))

    def test_dijkstra2(self):
        graph = {'a': {'b': 1, 'c': 3, 'd': 8},
                 'b': {'c': 1, 'd': 8},
                 'c': {'d': 5},
                 'd': {}}
        self.assertEqual(({'a': 0, 'c': 2, 'b': 1, 'd': 7}, {'c': 'b', 'b': 'a', 'd': 'c'}),
                         Dijkstra.dijkstra(graph, 'a', 'd'))

    def test_dijkstra3(self):
        graph = {'a': {'b': 1, 'e': 14, 'g': 1},
                 'b': {'c': 1, 'd': 2},
                 'c': {'e': 5},
                 'd': {'e': 3},
                 'e': {'f': 8},
                 'f': {'c': 4},
                 'g': {'f': 3}}
        self.assertEqual(({'a': 0, 'c': 2, 'b': 1, 'e': 6, 'd': 3, 'g': 1, 'f': 4},
                          {'c': 'b', 'b': 'a', 'e': 'd', 'd': 'b', 'g': 'a', 'f': 'g'}),
                         Dijkstra.dijkstra(graph, 'a', 'e'))

    def test_dijkstra4(self):
        graph = {'a': {'b': 1, 'e': 14, 'g': 1},
                 'b': {'c': 1, 'd': 2},
                 'c': {'e': 5},
                 'd': {'e': 3},
                 'e': {'f': 8},
                 'f': {'c': 4},
                 'g': {'f': 3}}
        self.assertEqual(({'c': 1, 'b': 0, 'e': 5, 'd': 2},
                          {'c': 'b', 'e': 'd', 'd': 'b'}),
                         Dijkstra.dijkstra(graph, 'b', 'e'))

    def test_dijkstra5(self):
        graph = {'a': {'b': 1, 'c': 3, 'd': 8},
                 'b': {'c': 1, 'd': 8},
                 'c': {'d': 1},
                 'd': {}}
        self.assertEqual(({'b': 0, 'c': 1, 'd': 2}, {'c': 'b', 'd': 'c'}),
                         Dijkstra.dijkstra(graph, 'b', 'd'))