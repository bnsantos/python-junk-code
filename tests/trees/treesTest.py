__author__ = 'bruno'
import unittest

import algorithms.trees.trees as Trees


class TestTrees(unittest.TestCase):
    def setUp(self):
        pass

    def test_binary_search_tree_1(self):
        b_tree = Trees.BinarySearchTree(Trees.IntBinaryNode(None, None, 10))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 2))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 12))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 11))

        self.assertEqual(11, b_tree.find_node(11))
        self.assertEqual(5, b_tree.find_node(5))
        self.assertEqual(None, b_tree.find_node(15))

    def test_binary_search_tree_2(self):
        b_tree = Trees.BinarySearchTree(Trees.IntBinaryNode(None, None, 10))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 2))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 1))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 20))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 12))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 11))

        self.assertEqual(11, b_tree.find_node(11))
        self.assertEqual(5, b_tree.find_node(5))
        self.assertEqual(None, b_tree.find_node(15))

    def test_binary_search_tree_3(self):
        b_tree = Trees.BinarySearchTree(Trees.IntBinaryNode(None, None, 10))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 2))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 1))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 20))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 12))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 11))

        self.assertEqual(11, b_tree.find_node(11))
        self.assertEqual(5, b_tree.find_node(5))
        self.assertEqual(True, b_tree.delete_node(Trees.IntBinaryNode(None, None, 1)))
        self.assertEqual(None, b_tree.find_node(1))

    def test_binary_search_tree_4(self):
        b_tree = Trees.BinarySearchTree(Trees.IntBinaryNode(None, None, 10))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 2))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 1))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 20))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 15))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 14))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 17))

        self.assertEqual(15, b_tree.find_node(15))
        self.assertEqual(5, b_tree.find_node(5))
        self.assertEqual(True, b_tree.delete_node(Trees.IntBinaryNode(None, None, 5)))
        self.assertEqual(5, b_tree.find_node(5))

    def test_binary_search_tree_5(self):
        b_tree = Trees.BinarySearchTree(Trees.IntBinaryNode(None, None, 10))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 2))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 1))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 20))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 15))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 14))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 17))

        self.assertEqual(15, b_tree.find_node(15))
        self.assertEqual(5, b_tree.find_node(5))
        self.assertEqual(True, b_tree.delete_node(Trees.IntBinaryNode(None, None, 5)))
        self.assertEqual(5, b_tree.find_node(5))
        self.assertEqual(True, b_tree.delete_node(Trees.IntBinaryNode(None, None, 5)))
        self.assertEqual(None, b_tree.find_node(5))

    def test_binary_search_tree_6(self):
        b_tree = Trees.BinarySearchTree(Trees.IntBinaryNode(None, None, 10))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 2))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 1))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 20))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 5))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 15))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 14))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 17))

        self.assertEqual(15, b_tree.find_node(15))
        self.assertEqual(20, b_tree.find_node(20))
        self.assertEqual(True, b_tree.delete_node(Trees.IntBinaryNode(None, None, 20)))
        self.assertEqual(None, b_tree.find_node(20))
        self.assertEqual(False, b_tree.delete_node(Trees.IntBinaryNode(None, None, 20)))

    def test_binary_search_tree_7(self):
        b_tree = Trees.BinarySearchTree(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 20))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 4))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 22))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 9))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 17))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 10))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 15))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 19))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 16))

        self.assertEqual(15, b_tree.find_node(15))
        self.assertEqual(13, b_tree.find_node(13))
        self.assertEqual(True, b_tree.delete_node(Trees.IntBinaryNode(None, None, 13)))
        self.assertEqual(13, b_tree.find_node(13))
        self.assertEqual(True, b_tree.delete_node(Trees.IntBinaryNode(None, None, 13)))
        self.assertEqual(None, b_tree.find_node(13))

    def test_binary_search_tree_8(self):
        b_tree = Trees.BinarySearchTree(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 20))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 4))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 22))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 9))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 17))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 10))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 15))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 19))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 16))

        self.assertEqual([8, 4, 20, 13, 9, 8, 10, 17, 15, 13, 16, 19, 22], b_tree.print_pre_order())

    def test_binary_search_tree_9(self):
        b_tree = Trees.BinarySearchTree(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 20))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 4))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 22))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 9))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 17))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 10))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 15))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 19))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 16))

        self.assertEqual([4, 8, 8, 9, 10, 13, 13, 15, 16, 17, 19, 20, 22], b_tree.print_in_order())

    def test_binary_search_tree_10(self):
        b_tree = Trees.BinarySearchTree(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 20))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 4))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 22))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 9))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 17))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 10))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 8))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 15))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 19))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 13))
        b_tree.add_node(Trees.IntBinaryNode(None, None, 16))

        self.assertEqual([4, 8, 10, 9, 13, 16, 15, 19, 17, 13, 22, 20, 8], b_tree.print_post_order())

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