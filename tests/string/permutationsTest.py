__author__ = 'bruno'
import unittest
import algorithms.string.permutations as Permutations


class TestPermutations(unittest.TestCase):
    def setUp(self):
        pass

    def test_permutations_1(self):
        self.assertEqual(['a'], Permutations.permutations('a'))

    def test_permutations_2(self):
        self.assertEqual(['aa', 'aa'], Permutations.permutations('aa'))

    def test_permutations_3(self):
        self.assertEqual(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'], Permutations.permutations('abc'))

    def test_permutations_4(self):
        out_array = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda',
                     'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb',
                     'dbac', 'dbca', 'dcab', 'dcba']
        self.assertEqual(out_array, Permutations.permutations('abcd'))

    def test_permutations_5(self):
        out_array = ['aeiou', 'aeiuo', 'aeoiu', 'aeoui', 'aeuio', 'aeuoi', 'aieou', 'aieuo', 'aioeu',
                     'aioue', 'aiueo', 'aiuoe', 'aoeiu', 'aoeui', 'aoieu', 'aoiue', 'aouei', 'aouie',
                     'aueio', 'aueoi', 'auieo', 'auioe', 'auoei', 'auoie', 'eaiou', 'eaiuo', 'eaoiu',
                     'eaoui', 'eauio', 'eauoi', 'eiaou', 'eiauo', 'eioau', 'eioua', 'eiuao', 'eiuoa',
                     'eoaiu', 'eoaui', 'eoiau', 'eoiua', 'eouai', 'eouia', 'euaio', 'euaoi', 'euiao',
                     'euioa', 'euoai', 'euoia', 'iaeou', 'iaeuo', 'iaoeu', 'iaoue', 'iaueo', 'iauoe',
                     'ieaou', 'ieauo', 'ieoau', 'ieoua', 'ieuao', 'ieuoa', 'ioaeu', 'ioaue', 'ioeau',
                     'ioeua', 'iouae', 'iouea', 'iuaeo', 'iuaoe', 'iueao', 'iueoa', 'iuoae', 'iuoea',
                     'oaeiu', 'oaeui', 'oaieu', 'oaiue', 'oauei', 'oauie', 'oeaiu', 'oeaui', 'oeiau',
                     'oeiua', 'oeuai', 'oeuia', 'oiaeu', 'oiaue', 'oieau', 'oieua', 'oiuae', 'oiuea',
                     'ouaei', 'ouaie', 'oueai', 'oueia', 'ouiae', 'ouiea', 'uaeio', 'uaeoi', 'uaieo',
                     'uaioe', 'uaoei', 'uaoie', 'ueaio', 'ueaoi', 'ueiao', 'ueioa', 'ueoai', 'ueoia',
                     'uiaeo', 'uiaoe', 'uieao', 'uieoa', 'uioae', 'uioea', 'uoaei', 'uoaie', 'uoeai',
                     'uoeia', 'uoiae', 'uoiea']
        self.assertEqual(out_array, Permutations.permutations('aeiou'))