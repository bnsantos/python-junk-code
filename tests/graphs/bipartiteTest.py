__author__ = 'bruno'
import unittest

import algorithms.graphs.bipartite as Bipartite


class TestBipartite(unittest.TestCase):
    def setUp(self):
        pass

    def test_bipartite_1(self):
        edges = [(1, 2), (2, 3), (1, 4), (2, 5), (3, 8), (5, 6)]
        graph = {}
        for n1, n2 in edges:
            Bipartite.make_link(graph, n1, n2)

        self.assertEqual([1, 3, 5] or [2, 4, 6, 8], Bipartite.bipartite(graph))

    def test_bipartite_2(self):
        edges = [(1, 2), (2, 3), (1, 3)]
        graph = {}
        for n1, n2 in edges:
            Bipartite.make_link(graph, n1, n2)
        self.assertEqual(None, Bipartite.bipartite(graph))