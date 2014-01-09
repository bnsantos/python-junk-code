__author__ = 'bruno'
import algorithms.graphs.clusteringCoefficient as ClusteringCoefficient
import algorithms.graphs.graph as Graph
import unittest


class TestClusteringCoefficient(unittest.TestCase):
    def setUp(self):
        pass

    def test_clustering_coefficient1(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h')])
        self.assertEqual(0.2916666666666667, ClusteringCoefficient.graph_clustering_coefficient(graph))

    def test_clustering_coefficient2(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h'),
                                  ('e', 'a')])
        self.assertEqual(0.20833333333333331, ClusteringCoefficient.graph_clustering_coefficient(graph))

    def test_clustering_coefficient3(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h'),
            ('h', 'i'), ('h', 'j'), ('j', 'm'), ('m', 'a')])
        self.assertEqual(0.1515151515151515, ClusteringCoefficient.graph_clustering_coefficient(graph))

    def test_clustering_coefficient4(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h')])
        self.assertEqual(0, ClusteringCoefficient.graph_clustering_coefficient(graph))

    def test_clustering_coefficient5(self):
        graph = Graph.make_graph([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')])
        self.assertEqual(0, ClusteringCoefficient.graph_clustering_coefficient(graph))

    def test_clustering_coefficient6(self):
        graph = Graph.make_graph([('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')])
        self.assertEqual(1, ClusteringCoefficient.clustering_coefficient(graph, 'a'))

    def test_clustering_coefficient7(self):
        graph = Graph.make_graph([('a', 'b'), ('a', 'c'), ('a', 'd')])
        self.assertEqual(0, ClusteringCoefficient.graph_clustering_coefficient(graph))

    def test_clustering_coefficient8(self):
        graph = Graph.make_graph([('a', 'b'), ('a', 'c'), ('a', 'd'), ('c', 'd')])
        self.assertEqual(0.3333333333333333, ClusteringCoefficient.clustering_coefficient(graph, 'a'))

    def test_clustering_coefficient9(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h')])
        self.assertEqual(0.2916666666666667, ClusteringCoefficient.graph_clustering_coefficient(graph))

    def test_clustering_coefficient10(self):
        graph = Graph.make_graph([('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h')])
        self.assertEqual(0.2916666666666667, ClusteringCoefficient.graph_clustering_coefficient(graph))