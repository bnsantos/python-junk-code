__author__ = 'bruno'
import unittest

import algorithms.rectangleOverlap as Overlap


class TestRectangleOverlap(unittest.TestCase):
    def setUp(self):
        pass

    def test_rectangle_overlap1(self):
        rect1 = Overlap.Rect(Overlap.Point(0, 2), Overlap.Point(10, 0))
        rect2 = Overlap.Rect(Overlap.Point(3, 3), Overlap.Point(5, -3))
        self.assertTrue(Overlap.Rect.overlap(rect1, rect2))

    def test_rectangle_overlap2(self):
        rect1 = Overlap.Rect(Overlap.Point(0, 3), Overlap.Point(3, 0))
        rect2 = Overlap.Rect(Overlap.Point(1, 4), Overlap.Point(4, 1))
        self.assertTrue(Overlap.Rect.overlap(rect1, rect2))

    def test_rectangle_overlap3(self):
        rect1 = Overlap.Rect(Overlap.Point(0, 3), Overlap.Point(5, 0))
        rect2 = Overlap.Rect(Overlap.Point(1, 5), Overlap.Point(4, 2))
        self.assertTrue(Overlap.Rect.overlap(rect1, rect2))

    def test_rectangle_overlap4(self):
        rect1 = Overlap.Rect(Overlap.Point(0, 8), Overlap.Point(8, 0))
        rect2 = Overlap.Rect(Overlap.Point(2, 5), Overlap.Point(5, 2))
        self.assertTrue(Overlap.Rect.overlap(rect1, rect2))

    def test_rectangle_overlap5(self):
        rect1 = Overlap.Rect(Overlap.Point(0, 1), Overlap.Point(1, 0))
        rect2 = Overlap.Rect(Overlap.Point(2, 2), Overlap.Point(3, 1))
        self.assertFalse(Overlap.Rect.overlap(rect1, rect2))

    def test_rectangle_overlap6(self):
        rect1 = Overlap.Rect(Overlap.Point(0, 5), Overlap.Point(5, 0))
        rect2 = Overlap.Rect(Overlap.Point(0, -1), Overlap.Point(5, -3))
        self.assertFalse(Overlap.Rect.overlap(rect1, rect2))

    def test_rectangle_overlap7(self):
        rect1 = Overlap.Rect(Overlap.Point(3, 1), Overlap.Point(5, 0))
        rect2 = Overlap.Rect(Overlap.Point(2, 2), Overlap.Point(4, -1))
        self.assertTrue(Overlap.Rect.overlap(rect1, rect2))

    def test_rectangle_overlap8(self):
        rect1 = Overlap.Rect(Overlap.Point(0, 8), Overlap.Point(2, 2))
        rect2 = Overlap.Rect(Overlap.Point(0, 0), Overlap.Point(-3, -3))
        self.assertFalse(Overlap.Rect.overlap(rect1, rect2))

    def test_rectangle_overlap9(self):
        rect1 = Overlap.Rect(Overlap.Point(1, 1), Overlap.Point(2, 0))
        rect2 = Overlap.Rect(Overlap.Point(2, 2), Overlap.Point(3, 3))
        self.assertFalse(Overlap.Rect.overlap(rect1, rect2))

    def test_rectangle_overlap10(self):
        rect1 = Overlap.Rect(Overlap.Point(5, 5), Overlap.Point(6, 3))
        rect2 = Overlap.Rect(Overlap.Point(2, 2), Overlap.Point(3, 0))
        self.assertFalse(Overlap.Rect.overlap(rect1, rect2))