__author__ = 'bruno'
import algorithms.peasantMultiplication as PeasantMultiplication
import unittest


class TestPeasantMultiplication(unittest.TestCase):
    def setUp(self):
        pass

    def test_peasant_multiplication1(self):
        self.assertEqual(1, PeasantMultiplication.russian(1, 1))

    def test_peasant_multiplication2(self):
        self.assertEqual(0, PeasantMultiplication.russian(1, 0))

    def test_peasant_multiplication3(self):
        self.assertEqual(0, PeasantMultiplication.russian(0, 1))

    def test_peasant_multiplication4(self):
        self.assertEqual(10, PeasantMultiplication.russian(10, 1))

    def test_peasant_multiplication5(self):
        self.assertEqual(30, PeasantMultiplication.russian(5, 6))

    def test_peasant_multiplication6(self):
        self.assertEqual(144, PeasantMultiplication.russian(12, 12))

    def test_peasant_multiplication7(self):
        self.assertEqual(800, PeasantMultiplication.russian(8, 100))

    def test_peasant_multiplication8(self):
        self.assertEqual(310104, PeasantMultiplication.russian(876, 354))

    def test_peasant_multiplication9(self):
        self.assertEqual(122166, PeasantMultiplication.russian(99, 1234))

    def test_peasant_multiplication10(self):
        self.assertEqual(1219326448286845269, PeasantMultiplication.russian(9876544321, 123456789))