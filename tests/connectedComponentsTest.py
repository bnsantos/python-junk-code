__author__ = 'bruno'
import algorithms.graphs.connectedComponents as ConnectedComponents
import algorithms.graphs.graph as Graph
import unittest


class TestConnectedComponents(unittest.TestCase):
    def setUp(self):
        pass

    def test_connectedComponents1(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h')])
        self.assertEqual({'a': 4, 'b': 4}, ConnectedComponents.list_component_sizes(graph))

    def test_connectedComponents2(self):
        graph = Graph.make_graph([('a', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h')])
        self.assertEqual({'a': 3, 'b': 4}, ConnectedComponents.list_component_sizes(graph))

    def test_connectedComponents3(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h'),
            ('k', 'l'), ('k', 'm'), ('l', 'm'), ('m', 'o')])
        self.assertEqual({'a': 4, 'b': 4, 'k': 4}, ConnectedComponents.list_component_sizes(graph))

    def test_connectedComponents4(self):
        graph = Graph.make_graph([('a', 'b'), ('b', 'c'), ('c', 'd')])
        self.assertEqual({'a': 4}, ConnectedComponents.list_component_sizes(graph))

    def test_connectedComponents5(self):
        graph = Graph.make_graph([('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'g'), ('d', 'h')])
        self.assertEqual({'a': 8}, ConnectedComponents.list_component_sizes(graph))

    def test_connectedComponents6(self):
        graph = Graph.make_graph([('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'e'), ('b', 'f'), ('k', 'g'), ('k', 'h')])
        self.assertEqual({'a': 6, 'g': 3}, ConnectedComponents.list_component_sizes(graph))

    def test_connectedComponents7(self):
        graph = Graph.make_graph([('a', 'b'), ('c', 'd'), ('d', 'g'), ('g', 'c'), ('f', 'e'), ('e', 'h')])
        self.assertEqual({'a': 2, 'c': 3, 'e': 3}, ConnectedComponents.list_component_sizes(graph))

    def test_connectedComponents8(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e')])
        self.assertEqual({'a': 4, 'b': 3}, ConnectedComponents.list_component_sizes(graph))

    def test_connectedComponents9(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h'),
                                  ('h', 'i'), ('i', 'b'), ('b', 'j')])
        self.assertEqual({'a': 4, 'b': 6}, ConnectedComponents.list_component_sizes(graph))

    def test_connectedComponents10(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('b', 'f'), ('f', 'e'), ('e', 'h')])
        self.assertEqual({'a': 3, 'b': 4}, ConnectedComponents.list_component_sizes(graph))