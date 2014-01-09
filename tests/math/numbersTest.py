__author__ = 'bruno'
import algorithms.math.numbers as Numbers
import unittest


class TestNumberYear(unittest.TestCase):
    def setUp(self):
        pass

    def test_decimal_to_roman1(self):
        self.assertEqual('X', Numbers.decimal_to_roman(10))

    def test_decimal_to_roman2(self):
        self.assertEqual('XII', Numbers.decimal_to_roman(12))

    def test_decimal_to_roman3(self):
        self.assertEqual('I', Numbers.decimal_to_roman(1))

    def test_decimal_to_roman4(self):
        self.assertEqual('MM', Numbers.decimal_to_roman(2000))

    def test_decimal_to_roman5(self):
        self.assertEqual('MMCCCXLV', Numbers.decimal_to_roman(2345))

    def test_decimal_to_roman6(self):
        self.assertEqual('DLV', Numbers.decimal_to_roman(555))

    def test_decimal_to_roman7(self):
        self.assertEqual('CCXXII', Numbers.decimal_to_roman(222))

    def test_decimal_to_roman8(self):
        self.assertEqual('LXXXVII', Numbers.decimal_to_roman(87))

    def test_decimal_to_roman9(self):
        self.assertEqual('XVII', Numbers.decimal_to_roman(17))

    def test_decimal_to_roman10(self):
        self.assertEqual('CXCIX', Numbers.decimal_to_roman(199))