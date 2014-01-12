__author__ = 'bruno'
import unittest
import algorithms.trees.binaryTree as Tree


class TestBinaryTrees(unittest.TestCase):
    def setUp(self):
        pass

    def test_binary_tree_1(self):
        root = Tree.IntBinaryNode(Tree.IntBinaryNode(
            Tree.IntBinaryNode(Tree.IntBinaryNode(None, None, 1), Tree.IntBinaryNode(None, None, 2), 3),
            Tree.IntBinaryNode(Tree.IntBinaryNode(None, None, 18), Tree.IntBinaryNode(None, None, 6), 25), 11),
            Tree.IntBinaryNode(Tree.IntBinaryNode(Tree.IntBinaryNode(None, None, 28),
                                                  Tree.IntBinaryNode(None, None, 13), 17),
                               Tree.IntBinaryNode(Tree.IntBinaryNode(None, None, 27),
                                                  Tree.IntBinaryNode(None, None, 23), 9),
                               8), 10)
        tree = Tree.BinarySearchTree(root)

        self.assertEqual(True, tree.heapify_binary_tree())
        self.assertEqual([11, 6, 13, 2, 17, 8, 18, 1, 23, 9, 25, 3, 27, 10, 28], tree.print_in_order())