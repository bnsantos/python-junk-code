__author__ = 'bruno'
import unittest
import algorithms.string.telephoneString as Telephone


class TestTelephoneString(unittest.TestCase):
    def setUp(self):
        pass

    def test_telephone_string_1(self):
        self.assertEqual([''], Telephone.print_telephone_words_recursive('1'))

    def test_telephone_string_2(self):
        self.assertEqual(['A', 'B', 'C'], Telephone.print_telephone_words_recursive('2'))

    def test_telephone_string_3(self):
        self.assertEqual(['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF'],
                         Telephone.print_telephone_words_recursive('23'))

    def test_telephone_string_4(self):
        result = ['ADG', 'ADH', 'ADI', 'AEG', 'AEH', 'AEI', 'AFG', 'AFH', 'AFI', 'BDG', 'BDH', 'BDI', 'BEG', 'BEH',
                  'BEI', 'BFG', 'BFH', 'BFI', 'CDG', 'CDH', 'CDI', 'CEG', 'CEH', 'CEI', 'CFG', 'CFH', 'CFI']
        self.assertEqual(result, Telephone.print_telephone_words_recursive('234'))

    def test_telephone_string_5(self):
        result = ['ADGJ', 'ADGK', 'ADGL', 'ADHJ', 'ADHK', 'ADHL', 'ADIJ', 'ADIK', 'ADIL', 'AEGJ', 'AEGK', 'AEGL',
                  'AEHJ', 'AEHK', 'AEHL', 'AEIJ', 'AEIK', 'AEIL', 'AFGJ', 'AFGK', 'AFGL', 'AFHJ', 'AFHK', 'AFHL',
                  'AFIJ', 'AFIK', 'AFIL', 'BDGJ', 'BDGK', 'BDGL', 'BDHJ', 'BDHK', 'BDHL', 'BDIJ', 'BDIK', 'BDIL',
                  'BEGJ', 'BEGK', 'BEGL', 'BEHJ', 'BEHK', 'BEHL', 'BEIJ', 'BEIK', 'BEIL', 'BFGJ', 'BFGK', 'BFGL',
                  'BFHJ', 'BFHK', 'BFHL', 'BFIJ', 'BFIK', 'BFIL', 'CDGJ', 'CDGK', 'CDGL', 'CDHJ', 'CDHK', 'CDHL',
                  'CDIJ', 'CDIK', 'CDIL', 'CEGJ', 'CEGK', 'CEGL', 'CEHJ', 'CEHK', 'CEHL', 'CEIJ', 'CEIK', 'CEIL',
                  'CFGJ', 'CFGK', 'CFGL', 'CFHJ', 'CFHK', 'CFHL', 'CFIJ', 'CFIK', 'CFIL']
        self.assertEqual(result, Telephone.print_telephone_words_recursive('2345'))

    def test_telephone_string_iterative_1(self):
        self.assertEqual([''], Telephone.print_telephone_words_iterative('1'))

    def test_telephone_string_iterative_2(self):
        self.assertEqual(['A', 'B', 'C'], Telephone.print_telephone_words_iterative('2'))

    def test_telephone_string_iterative_3(self):
        self.assertEqual(['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF'],
                         Telephone.print_telephone_words_iterative('23'))

    def test_telephone_string_iterative_4(self):
        result = ['ADG', 'ADH', 'ADI', 'AEG', 'AEH', 'AEI', 'AFG', 'AFH', 'AFI', 'BDG', 'BDH', 'BDI', 'BEG', 'BEH',
                  'BEI', 'BFG', 'BFH', 'BFI', 'CDG', 'CDH', 'CDI', 'CEG', 'CEH', 'CEI', 'CFG', 'CFH', 'CFI']
        self.assertEqual(result, Telephone.print_telephone_words_iterative('234'))

    def test_telephone_string_iterative_5(self):
        result = ['ADGJ', 'ADGK', 'ADGL', 'ADHJ', 'ADHK', 'ADHL', 'ADIJ', 'ADIK', 'ADIL', 'AEGJ', 'AEGK', 'AEGL',
                  'AEHJ', 'AEHK', 'AEHL', 'AEIJ', 'AEIK', 'AEIL', 'AFGJ', 'AFGK', 'AFGL', 'AFHJ', 'AFHK', 'AFHL',
                  'AFIJ', 'AFIK', 'AFIL', 'BDGJ', 'BDGK', 'BDGL', 'BDHJ', 'BDHK', 'BDHL', 'BDIJ', 'BDIK', 'BDIL',
                  'BEGJ', 'BEGK', 'BEGL', 'BEHJ', 'BEHK', 'BEHL', 'BEIJ', 'BEIK', 'BEIL', 'BFGJ', 'BFGK', 'BFGL',
                  'BFHJ', 'BFHK', 'BFHL', 'BFIJ', 'BFIK', 'BFIL', 'CDGJ', 'CDGK', 'CDGL', 'CDHJ', 'CDHK', 'CDHL',
                  'CDIJ', 'CDIK', 'CDIL', 'CEGJ', 'CEGK', 'CEGL', 'CEHJ', 'CEHK', 'CEHL', 'CEIJ', 'CEIK', 'CEIL',
                  'CFGJ', 'CFGK', 'CFGL', 'CFHJ', 'CFHK', 'CFHL', 'CFIJ', 'CFIK', 'CFIL']
        self.assertEqual(result, Telephone.print_telephone_words_iterative('2345'))