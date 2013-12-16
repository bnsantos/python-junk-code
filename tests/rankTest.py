__author__ = 'bruno'
import algorithms.statistics.rank as Rank
import unittest


class TestRank(unittest.TestCase):
    def setUp(self):
        pass

    def test_rank1(self):
        self.assertEqual(9, Rank.rank([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 66))

    def test_rank2(self):
        self.assertEqual(1, Rank.rank([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 11))

    def test_rank3(self):
        self.assertEqual(13, Rank.rank([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 91))

    def test_rank4(self):
        self.assertEqual(1, Rank.rank([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 11))

    def test_rank5(self):
        self.assertEqual(3, Rank.rank([99, 74, 65, 23, 30, 10, 6, 48, 234, 52], 23))

    def test_rank6(self):
        self.assertEqual(6, Rank.rank([99, 102, 48, 83, 52, 30, 2, 17, 68, 12, 44, 39], 44))

    def test_rank7(self):
        self.assertEqual(4, Rank.rank([12, 32, 23, 34, 54, 43, 33, 56, 48, 87, 99], 33))

    def test_rank8(self):
        self.assertEqual(4, Rank.rank([9, 8, 5, 2, 3, 5, 7, 3, 4], 4))

    def test_rank9(self):
        self.assertEqual(6, Rank.rank([-1, -15, 2, 99, 84, -87, -33, 46, 27], 27))

    def test_rank10(self):
        self.assertEqual(6, Rank.rank([99, 88, 77, 66, 44, 55, 33, 22, 11, -13, -15, 18, -98], 22))

    def test_partition1(self):
        self.assertEqual([31, 45, 51, 28, 33, 11, 27, 36, 66, 91, 66, 82, 89, 84],
                         Rank.partition([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 66))

    def test_partition2(self):
        self.assertEqual([11, 31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36],
                         Rank.partition([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 11))

    def test_partition3(self):
        self.assertEqual([31, 45, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36, 91, 91],
                         Rank.partition([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 91))

    def test_partition4(self):
        self.assertEqual([11, 31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36],
                         Rank.partition([31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36], 11))

    def test_partition5(self):
        self.assertEqual([10, 6, 23, 99, 74, 65, 23, 30, 48, 234, 52],
                         Rank.partition([99, 74, 65, 23, 30, 10, 6, 48, 234, 52], 23))

    def test_partition6(self):
        self.assertEqual([30, 2, 17, 12, 39, 44, 99, 102, 48, 83, 52, 68, 44],
                         Rank.partition([99, 102, 48, 83, 52, 30, 2, 17, 68, 12, 44, 39], 44))

    def test_partition7(self):
        self.assertEqual([12, 32, 23, 33, 34, 54, 43, 33, 56, 48, 87, 99],
                         Rank.partition([12, 32, 23, 34, 54, 43, 33, 56, 48, 87, 99], 33))

    def test_partition8(self):
        self.assertEqual([2, 3, 3, 4, 9, 8, 5, 5, 7, 4], Rank.partition([9, 8, 5, 2, 3, 5, 7, 3, 4], 4))

    def test_partition9(self):
        self.assertEqual([-1, -15, 2, -87, -33, 27, 99, 84, 46, 27],
                         Rank.partition([-1, -15, 2, 99, 84, -87, -33, 46, 27], 27))

    def test_partition10(self):
        self.assertEqual([11, -13, -15, 18, -98, 22, 99, 88, 77, 66, 44, 55, 33, 22],
                         Rank.partition([99, 88, 77, 66, 44, 55, 33, 22, 11, -13, -15, 18, -98], 22))