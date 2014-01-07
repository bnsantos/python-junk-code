__author__ = 'bruno'
import algorithms.linkedList as LinkedList
import unittest


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        pass

    def test_linked_list_1(self):
        linked_list = LinkedList.LinkedList(LinkedList.Element(5))
        linked_list.add(LinkedList.Element(4))
        linked_list.add(LinkedList.Element(3))
        linked_list.add(LinkedList.Element(2))
        linked_list.add(LinkedList.Element(1))
        self.assertEqual(True, linked_list.remove(4))
        self.assertEqual(True, linked_list.remove(3))
        self.assertEqual(True, linked_list.remove(2))
        self.assertEqual(True, linked_list.remove(1))
        self.assertEqual(True, linked_list.remove(0))
        self.assertEqual(True, linked_list.empty())

    def test_linked_list_2(self):
        linked_list = LinkedList.LinkedList(LinkedList.Element(0))
        for i in range(1, 11):
            linked_list.add(LinkedList.Element(i))

        self.assertEqual(False, linked_list.empty())

    def test_linked_list_3(self):
        linked_list = LinkedList.LinkedList(LinkedList.Element(0))
        for i in range(1, 10):
            linked_list.add(LinkedList.Element(i))

        self.assertEqual(5, linked_list.find_m_to_last_element(5))

    def test_linked_list_4(self):
        linked_list = LinkedList.LinkedList(LinkedList.Element(0))
        for i in range(1, 500):
            linked_list.add(LinkedList.Element(i))

        self.assertEqual(500, linked_list.count())
        self.assertEqual(495, linked_list.find_m_to_last_element(5))

    def test_linked_list_5(self):
        linked_list = LinkedList.LinkedList(LinkedList.Element(0))
        for i in range(1, 500):
            linked_list.add(LinkedList.Element(i))
        self.assertEqual(500, linked_list.count())

        for i in range(100):
            self.assertEqual(True, linked_list.remove(0))
        self.assertEqual(400, linked_list.count())
        self.assertEqual(485, linked_list.find_m_to_last_element(15))

    def test_linked_list_6(self):
        linked_list = LinkedList.LinkedList(LinkedList.Element(0))
        for i in range(1, 500):
            linked_list.add(LinkedList.Element(i))
        self.assertEqual(500, linked_list.count())

        for i in range(300):
            self.assertEqual(True, linked_list.remove(0))
        self.assertEqual(200, linked_list.count())
        self.assertEqual(400, linked_list.find_m_to_last_element(100))

    def test_linked_list_7(self):
        linked_list = LinkedList.LinkedList(LinkedList.Element(0))
        for i in range(1, 500):
            linked_list.add(LinkedList.Element(i))
        self.assertEqual(500, linked_list.count())

        for i in range(350):
            self.assertEqual(True, linked_list.remove(0))
        self.assertEqual(150, linked_list.count())

    def test_linked_list_8(self):
        linked_list = LinkedList.LinkedList(LinkedList.Element(0))
        for i in range(1, 500):
            linked_list.add(LinkedList.Element(i))
        self.assertEqual(500, linked_list.count())

        for i in range(300):
            self.assertEqual(True, linked_list.remove(0))
        self.assertEqual(200, linked_list.count())

        for i in range(300, 500):
            self.assertEqual(True, linked_list.remove(0))
        self.assertEqual(0, linked_list.count())

    def test_linked_list_9(self):
        linked_list = LinkedList.LinkedList(LinkedList.Element(0))
        for i in range(1, 500):
            linked_list.add(LinkedList.Element(i))
        self.assertEqual(500, linked_list.count())

        for i in range(350):
            self.assertEqual(True, linked_list.remove(0))
        self.assertEqual(150, linked_list.count())

    def test_linked_list_10(self):
        linked_list = LinkedList.LinkedList(LinkedList.Element(0))
        for i in range(1, 500):
            linked_list.add(LinkedList.Element(i))
        self.assertEqual(500, linked_list.count())

        for i in range(500):
            self.assertEqual(True, linked_list.remove(0))
        self.assertEqual(0, linked_list.count())

        self.assertEqual(False, linked_list.remove(0))