__author__ = 'bruno'
import unittest


class TestMostPopularName(unittest.TestCase):
    @staticmethod
    def read_file(input_file):
        girls_names = []
        boys_names = []
        for line in input_file.readlines():
            elem = line.strip().split(',')
            if elem[1] == 'M':
                boys_names.append((int(elem[2]), elem[0]))
            else:
                girls_names.append((int(elem[2]), elem[0]))

        girls_names.sort()
        boys_names.sort()
        return girls_names, boys_names

    def setUp(self):
        self.girls_names, self.boys_names = TestMostPopularName.read_file(open("input/yob1995"))

    def test_least_popular_girl_name(self):
        self.assertEqual('Aailiyah', self.girls_names[0][1])

    def test_2_least_popular_girl_name(self):
        self.assertEqual('Aalia', self.girls_names[1][1])

    def test_median_popular_girl_name(self):
        self.assertEqual('Imara', self.girls_names[len(self.girls_names)/2][1])

    def test_2_most_popular_girl_name(self):
        self.assertEqual('Ashley', self.girls_names[len(self.girls_names)-2][1])

    def test_most_popular_girl_name(self):
        self.assertEqual('Jessica', self.girls_names[len(self.girls_names)-1][1])

    def test_least_popular_boy_name(self):
        self.assertEqual('Aanand', self.boys_names[0][1])

    def test_2_least_popular_boy_name(self):
        self.assertEqual('Aaronn', self.boys_names[1][1])

    def test_median_popular_boy_name(self):
        self.assertEqual('Stephaun', self.boys_names[len(self.boys_names)/2][1])

    def test_2_most_popular_boy_name(self):
        self.assertEqual('Matthew', self.boys_names[len(self.boys_names)-2][1])

    def test_most_popular_boy_name(self):
        self.assertEqual('Michael', self.boys_names[len(self.boys_names)-1][1])