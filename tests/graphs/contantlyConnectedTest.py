__author__ = 'bruno'
import unittest
import algorithms.graphs.contantlyConnected as Connected


class TestConstantlyConnected(unittest.TestCase):
    def setUp(self):
        pass

    def test_constantly_connected_1(self):
        graph = {1: {2: 1}, 2: {1: 1}, 3: {4: 1}, 4: {3: 1}, 5: {}}
        processed = Connected.process_graph(graph)

        self.assertEqual(True, Connected.is_connected(processed, 1, 2))
        self.assertEqual(False, Connected.is_connected(processed, 1, 3))

    def test_constantly_connected_2(self):
        graph = {1: {2: 1, 3: 1}, 2: {1: 1}, 3: {4: 1, 1: 1}, 4: {3: 1}, 5: {}}
        processed = Connected.process_graph(graph)

        self.assertEqual(True, Connected.is_connected(processed, 1, 2))
        self.assertEqual(True, Connected.is_connected(processed, 1, 3))
        self.assertEqual(False, Connected.is_connected(processed, 1, 5))