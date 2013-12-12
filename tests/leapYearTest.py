__author__ = 'bruno'
import algorithms.leapYear as LeapYear
import unittest


class TestLeapYear(unittest.TestCase):
    def setUp(self):
        pass

    def test_leap_year1(self):
        self.assertEqual(True, LeapYear.leap_year(1804))

    def test_leap_year2(self):
        self.assertEqual(True, LeapYear.leap_year(1808))

    def test_leap_year3(self):
        self.assertEqual(True, LeapYear.leap_year(2020))

    def test_leap_year4(self):
        self.assertEqual(True, LeapYear.leap_year(1924))

    def test_leap_year5(self):
        self.assertEqual(True, LeapYear.leap_year(2000))

    def test_leap_year6(self):
        self.assertEqual(False, LeapYear.leap_year(1999))

    def test_leap_year7(self):
        self.assertEqual(False, LeapYear.leap_year(2055))

    def test_leap_year8(self):
        self.assertEqual(False, LeapYear.leap_year(2229))

    def test_leap_year9(self):
        self.assertEqual(False, LeapYear.leap_year(1990))

    def test_leap_year10(self):
        self.assertEqual(False, LeapYear.leap_year(1803))