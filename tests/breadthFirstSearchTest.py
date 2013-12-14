__author__ = 'bruno'
import algorithms.graphs.breadthFirstSearch as BreadthFirstSearch
import algorithms.graphs.graph as Graph
import unittest


class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        pass

    def test_breadthFirstSearch1(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h')])
        self.assertEqual([], BreadthFirstSearch.search(graph, 'a', 'b'))

    def test_breadthFirstSearch2(self):
        graph = Graph.make_graph([('a', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h')])
        self.assertEqual(['a', 'g'], BreadthFirstSearch.search(graph, 'a', 'g'))

    def test_breadthFirstSearch3(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h'),
            ('k', 'l'), ('k', 'm'), ('l', 'm'), ('m', 'o')])
        self.assertEqual(['a', 'g', 'c'], BreadthFirstSearch.search(graph, 'a', 'c'))

    def test_breadthFirstSearch4(self):
        graph = Graph.make_graph([('a', 'b'), ('b', 'c'), ('c', 'd')])
        self.assertEqual(['a', 'b', 'c', 'd'], BreadthFirstSearch.search(graph, 'a', 'd'))

    def test_breadthFirstSearch5(self):
        graph = Graph.make_graph([('a', 'b'), ('c', 'd'), ('d', 'g'), ('g', 'c'), ('f', 'e'), ('e', 'h'),
                                  ('l', 'm'), ('m', 'a'), ('a', 'n'), ('n', 'o')])
        self.assertEqual(['o', 'n', 'a', 'm', 'l'], BreadthFirstSearch.search(graph, 'o', 'l'))

    def test_breadthFirstSearch6(self):
        graph = Graph.make_graph([('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'e'), ('b', 'f'), ('k', 'g'), ('k', 'h')])
        self.assertEqual(['k', 'g'], BreadthFirstSearch.search(graph, 'k', 'g'))

    def test_breadthFirstSearch7(self):
        graph = Graph.make_graph([('a', 'b'), ('c', 'd'), ('d', 'g'), ('g', 'c'), ('f', 'e'), ('e', 'h'),
                                  ('l', 'm'), ('m', 'a'), ('a', 'n'), ('n', 'o')])
        self.assertEqual(['l', 'm', 'a', 'n', 'o'], BreadthFirstSearch.search(graph, 'l', 'o'))

    def test_breadthFirstSearch8(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('b', 'f'), ('f', 'e'), ('e', 'h'), ('h', 'a')])
        self.assertEqual(['h', 'a'], BreadthFirstSearch.search(graph, 'h', 'a'))

    def test_breadthFirstSearch9(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h'),
                                  ('h', 'i'), ('i', 'b'), ('b', 'j')])
        self.assertEqual(['i', 'b', 'j'], BreadthFirstSearch.search(graph, 'i', 'j'))

    def test_breadthFirstSearch10(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('b', 'f'), ('f', 'e'), ('e', 'h'), ('h', 'a')])
        self.assertEqual(['a', 'h'], BreadthFirstSearch.search(graph, 'a', 'h'))