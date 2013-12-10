__author__ = 'bruno'
import unittest
import sys
sys.path.insert(0, '../helper')
import helper.validateInput as ValidatedInput


class ValidateInputTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_validate_input_negative(self):
        self.assertEqual(False, ValidatedInput.validate_integer_positive_input(-2))

    def test_validate_input_positive(self):
        self.assertEqual(True, ValidatedInput.validate_integer_positive_input(2))

    def test_validate_input_string(self):
        self.assertEqual(False, ValidatedInput.validate_integer_positive_input('oi'))

    def test_validate_input_float(self):
        self.assertEqual(False, ValidatedInput.validate_integer_positive_input(2.0))