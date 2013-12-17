__author__ = 'bruno'
import algorithms.statistics.mode as Mode
import unittest


class TestMode(unittest.TestCase):
    def setUp(self):
        pass

    def test_mode1(self):
        self.assertEqual(5, Mode.mode([1, 2, 3, 4, 5, 6, 7, 8, 9, 5]))

    def test_mode2(self):
        self.assertEqual(9, Mode.mode([9, 9, 9, 9, 9, 9, 9, 9, 9]))

    def test_mode3(self):
        self.assertEqual('a', Mode.mode(['a', 'b', 'c', 'd', 'a', 'e', 'f', 'f', 'a']))

    def test_mode4(self):
        self.assertEqual(4, Mode.mode([4, 5, 6, 7,  8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]))

    def test_mode5(self):
        self.assertEqual(88, Mode.mode([1, 2, 3, 4, 5, 88, 7, 8, 9, 88, 9, 9, 88, 2, 3, 88]))

    def test_mode6(self):
        self.assertEqual(0, Mode.mode([0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]))

    def test_mode7(self):
        self.assertEqual(1, Mode.mode([1, 2, 3, 4, 5, 1, 7, 8, 9]))

    def test_mode8(self):
        self.assertEqual(10, Mode.mode([10]))

    def test_mode9(self):
        self.assertEqual(None, Mode.mode([]))

    def test_mode10(self):
        self.assertEqual(23, Mode.mode([1, 2, 23, 4, 5, 6, 7, 8, 9, 23, 23]))