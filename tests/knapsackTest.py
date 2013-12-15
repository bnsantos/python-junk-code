__author__ = 'bruno'
import algorithms.knapsack as Knapsack
import unittest


class TestKnapsack(unittest.TestCase):
    def setUp(self):
        pass

    def test_knapsack1(self):
        items = Knapsack.get_items(10)
        self.assertEqual([54, 27, 0, 0, 1, 1, 0, 0, 0, 0],
                         Knapsack.knapsack_dp(items, Knapsack.Bounty('sack', 0, 250, 250)))

    def test_knapsack2(self):
        items = Knapsack.get_items(15)
        self.assertEqual([83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 167, 0, 0],
                         Knapsack.knapsack_dp(items, Knapsack.Bounty('sack', 0, 500, 500)))

    def test_knapsack3(self):
        items = Knapsack.get_items(10)
        self.assertEqual([220, 110, 0, 0, 1, 2, 0, 0, 0, 0],
                         Knapsack.knapsack_dp(items, Knapsack.Bounty('sack', 0, 1000, 1000)))

    def test_knapsack4(self):
        items = Knapsack.get_items(15)
        self.assertEqual([16, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 33, 0, 0],
                         Knapsack.knapsack_dp(items, Knapsack.Bounty('sack', 0, 100, 100)))

    def test_knapsack5(self):
        items = Knapsack.get_items(10)
        self.assertEqual([10, 5, 0, 1, 0, 0, 0, 0, 0, 0],
                         Knapsack.knapsack_dp(items, Knapsack.Bounty('sack', 0, 50, 50)))

    def test_knapsack6(self):
        items = Knapsack.get_items(15)
        self.assertEqual([8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0],
                         Knapsack.knapsack_dp(items, Knapsack.Bounty('sack', 0, 50, 50)))

    def test_knapsack7(self):
        items = Knapsack.get_items(5)
        self.assertEqual([10, 5, 0, 1, 0],
                         Knapsack.knapsack_dp(items, Knapsack.Bounty('sack', 0, 50, 50)))

    def test_knapsack8(self):
        items = Knapsack.get_items(5)
        self.assertEqual([22, 11, 0, 0, 0],
                         Knapsack.knapsack_dp(items, Knapsack.Bounty('sack', 0, 100, 100)))

    def test_knapsack9(self):
        items = Knapsack.get_items(5)
        self.assertEqual([10, 5, 0, 1, 0],
                         Knapsack.knapsack_dp(items, Knapsack.Bounty('sack', 0, 50, 50)))

    def test_knapsack10(self):
        items = Knapsack.get_items(1)
        self.assertEqual([62],
                         Knapsack.knapsack_dp(items, Knapsack.Bounty('sack', 0, 250, 250)))