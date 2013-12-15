__author__ = 'bruno'
import algorithms.cripto.caesar as Caesar
import unittest


class TestCaesar(unittest.TestCase):

    def setUp(self):
        self.caesar = Caesar.Caesar()
        pass

    def test_caesar_encrypt1(self):
        self.assertEqual('', self.caesar.encrypt(''))

    def test_caesar_encrypt2(self):
        self.assertEqual('DDDDDDD', self.caesar.encrypt('aaaaaaa'))

    def test_caesar_encrypt3(self):
        self.assertEqual('JRQLQHUV', self.caesar.encrypt('go niners'))

    def test_caesar_encrypt4(self):
        self.assertEqual('LIBRXUHJRLQJWRVDQIUDQFLVFR', self.caesar.encrypt('if youre going to san francisco'))

    def test_caesar_encrypt5(self):
        self.assertEqual('III', self.caesar.encrypt('aaa', 8))

    def test_caesar_encrypt6(self):
        self.assertEqual('SHWHUSLSHUSLFNHGDSHFNRISLFNOHGSHSSHUV',
                         self.caesar.encrypt('Peter Piper picked a peck of pickled peppers'))

    def test_caesar_encrypt7(self):
        self.assertEqual('BRXFXVVLFXVVZHDOOFXVVIRUDVSDUDJXV',
                         self.caesar.encrypt('You cuss, I cuss, we all cuss, for asparagus'))

    def test_caesar_encrypt8(self):
        self.assertEqual('FOHDQFODPVFUDPPHGLQFOHDQFDQV',
                         self.caesar.encrypt('Clean clams crammed in clean cans'))

    def test_caesar_encrypt9(self):
        self.assertEqual('VLAVLFNKLFNVQLFNVLAVOLFNEULFNVZLWKSLFNVDQGVWLFNV',
                         self.caesar.encrypt('Six sick hicks nick six slick bricks with picks and sticks'))

    def test_caesar_encrypt10(self):
        self.assertEqual('SLFNBSHRSOHSLFNSHWHUSDQSHDQXWEXWWHUWLVWKHSHDQXWEXWWHUSLFNBSHRSOHSLFN',
                         self.caesar.encrypt('Picky people pick Peter Pan Peanut-Butter, '
                                             '"tis the peanut-butter picky people pick"'))