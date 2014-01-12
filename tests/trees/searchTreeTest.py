__author__ = 'bruno'
import unittest

import algorithms.trees.searchTree as Trees


class TestTrees(unittest.TestCase):
    def setUp(self):
        pass

    def test_bfs_tree_1(self):
        root = Trees.IntNode([], 10)
        root.add_child(Trees.IntNode([Trees.IntNode([], 4), Trees.IntNode([], 2),
                                      Trees.IntNode([], 6), Trees.IntNode([], 0)], 5))
        root.add_child(Trees.IntNode([Trees.IntNode([], 54), Trees.IntNode([], 43),
                                      Trees.IntNode([], 24), Trees.IntNode([], 23),
                                      Trees.IntNode([], 99), Trees.IntNode([], 22),
                                      Trees.IntNode(None, 100), Trees.IntNode(None, 18)], 21))
        root.add_child(Trees.IntNode([Trees.IntNode(None, 66), Trees.IntNode(None, 33),
                                      Trees.IntNode(None, 77), Trees.IntNode(None, 11),
                                      Trees.IntNode(None, 88), Trees.IntNode(None, 8),
                                      Trees.IntNode(None, 62), Trees.IntNode(None, 72),
                                      Trees.IntNode(None, 69), Trees.IntNode(None, 65),
                                      Trees.IntNode(None, 87), Trees.IntNode(None, 98),
                                      Trees.IntNode(None, 17), Trees.IntNode(None, 101),
                                      Trees.IntNode(None, 91), Trees.IntNode(None, 157)], 82))
        tree = Trees.Tree(root)
        self.assertEqual(True, tree.breadth_first_search(157))
        self.assertEqual(False, tree.breadth_first_search(200))
        self.assertEqual(True, tree.breadth_first_search(87))
        self.assertEqual(True, tree.breadth_first_search(0))

    def test_bfs_tree_2(self):
        root = Trees.IntNode([], 10)
        root.add_child(Trees.IntNode([Trees.IntNode([], 4), Trees.IntNode([], 2),
                                      Trees.IntNode([], 6), Trees.IntNode([], 0)], 5))
        root.add_child(Trees.IntNode([Trees.IntNode([], 54), Trees.IntNode([], 43),
                                      Trees.IntNode([], 24), Trees.IntNode([], 23),
                                      Trees.IntNode([], 99), Trees.IntNode([], 22),
                                      Trees.IntNode(None, 100), Trees.IntNode(None, 18)], 21))
        root.add_child(Trees.IntNode([Trees.IntNode(None, 66), Trees.IntNode(None, 33),
                                      Trees.IntNode(None, 77), Trees.IntNode(None, 11),
                                      Trees.IntNode(None, 88), Trees.IntNode(None, 8),
                                      Trees.IntNode(None, 62), Trees.IntNode(None, 72),
                                      Trees.IntNode(None, 69), Trees.IntNode(None, 65),
                                      Trees.IntNode(None, 87), Trees.IntNode(None, 98),
                                      Trees.IntNode(None, 17), Trees.IntNode(None, 101),
                                      Trees.IntNode(None, 91), Trees.IntNode(None, 157)], 82))
        tree = Trees.Tree(root)
        self.assertEqual(True, tree.depth_first_search(157))
        self.assertEqual(False, tree.depth_first_search(200))
        self.assertEqual(True, tree.depth_first_search(87))
        self.assertEqual(True, tree.depth_first_search(0))

    def test_bfs_tree_3(self):
        root = Trees.IntNode([], 10)
        root.add_child(Trees.IntNode([Trees.IntNode([Trees.IntNode([Trees.IntNode([], 543),
                                                                   Trees.IntNode([], 909),
                                                                   Trees.IntNode([], 887),
                                                                   Trees.IntNode([], 765)], 123)], 4),
                                      Trees.IntNode([Trees.IntNode([Trees.IntNode([], 232),
                                                                   Trees.IntNode([], 432),
                                                                   Trees.IntNode([], 747),
                                                                   Trees.IntNode([], 901)], 190)], 2),
                                      Trees.IntNode([Trees.IntNode([Trees.IntNode([], 222),
                                                                   Trees.IntNode([], 323),
                                                                   Trees.IntNode([], 167),
                                                                   Trees.IntNode([], 939)], 555)], 6),
                                      Trees.IntNode([Trees.IntNode([Trees.IntNode([], 999),
                                                                   Trees.IntNode([], 443),
                                                                   Trees.IntNode([], 442),
                                                                   Trees.IntNode([], 441)], 565)], 0)],
                                     5))
        root.add_child(Trees.IntNode([Trees.IntNode([], 54), Trees.IntNode([], 43),
                                      Trees.IntNode([], 24), Trees.IntNode([], 23),
                                      Trees.IntNode([], 99), Trees.IntNode([], 22),
                                      Trees.IntNode(None, 100), Trees.IntNode(None, 18)], 21))
        root.add_child(Trees.IntNode([Trees.IntNode(None, 66), Trees.IntNode(None, 33),
                                      Trees.IntNode(None, 77), Trees.IntNode(None, 11),
                                      Trees.IntNode(None, 88), Trees.IntNode(None, 8),
                                      Trees.IntNode(None, 62), Trees.IntNode(None, 72),
                                      Trees.IntNode(None, 69), Trees.IntNode(None, 65),
                                      Trees.IntNode(None, 87), Trees.IntNode(None, 98),
                                      Trees.IntNode(None, 17), Trees.IntNode(None, 101),
                                      Trees.IntNode(None, 91), Trees.IntNode(None, 157)], 82))
        tree = Trees.Tree(root)
        self.assertEqual(True, tree.depth_first_search(157))
        self.assertEqual(False, tree.depth_first_search(200))
        self.assertEqual(True, tree.depth_first_search(87))
        self.assertEqual(True, tree.depth_first_search(0))

    def test_bfs_tree_4(self):
        root = Trees.IntNode([], 10)
        root.add_child(Trees.IntNode([Trees.IntNode([Trees.IntNode([Trees.IntNode([], 543),
                                                                   Trees.IntNode([], 909),
                                                                   Trees.IntNode([], 887),
                                                                   Trees.IntNode([], 765)], 123)], 4),
                                      Trees.IntNode([Trees.IntNode([Trees.IntNode([], 232),
                                                                   Trees.IntNode([], 432),
                                                                   Trees.IntNode([], 747),
                                                                   Trees.IntNode([], 901)], 190)], 2),
                                      Trees.IntNode([Trees.IntNode([Trees.IntNode([], 222),
                                                                   Trees.IntNode([], 323),
                                                                   Trees.IntNode([], 167),
                                                                   Trees.IntNode([], 939)], 555)], 6),
                                      Trees.IntNode([Trees.IntNode([Trees.IntNode([], 999),
                                                                   Trees.IntNode([], 443),
                                                                   Trees.IntNode([], 442),
                                                                   Trees.IntNode([], 441)], 565)], 0)],
                                     5))
        root.add_child(Trees.IntNode([Trees.IntNode([], 54), Trees.IntNode([], 43),
                                      Trees.IntNode([], 24), Trees.IntNode([], 23),
                                      Trees.IntNode([], 99), Trees.IntNode([], 22),
                                      Trees.IntNode(None, 100), Trees.IntNode(None, 18)], 21))
        root.add_child(Trees.IntNode([Trees.IntNode(None, 66), Trees.IntNode(None, 33),
                                      Trees.IntNode(None, 77), Trees.IntNode(None, 11),
                                      Trees.IntNode(None, 88), Trees.IntNode(None, 8),
                                      Trees.IntNode(None, 62), Trees.IntNode(None, 72),
                                      Trees.IntNode(None, 69), Trees.IntNode(None, 65),
                                      Trees.IntNode(None, 87), Trees.IntNode(None, 98),
                                      Trees.IntNode(None, 17), Trees.IntNode(None, 101),
                                      Trees.IntNode(None, 91), Trees.IntNode(None, 157)], 82))
        tree = Trees.Tree(root)
        self.assertEqual(5, tree.get_height())