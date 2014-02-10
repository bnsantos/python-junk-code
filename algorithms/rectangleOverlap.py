__author__ = 'bruno'


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect(object):
    def __init__(self, ul, lr):
        self.ul = ul
        self.lr = lr

    @staticmethod
    def overlap(rect1, rect2):
        return rect1.ul.x <= rect2.lr.x and rect1.ul.y >= rect2.lr.y and rect1.lr.x >= rect2.ul.x \
            and rect1.lr.y <= rect2.ul.y