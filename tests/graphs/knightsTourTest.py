__author__ = 'bruno'
import unittest
import algorithms.graphs.knightsTour as KnightsTour


class TestKnightsTour(unittest.TestCase):
    def setUp(self):
        pass

    def test_knights_tour_1(self):
        graph = KnightsTour.knight_graph(4)