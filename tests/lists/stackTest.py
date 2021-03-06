__author__ = 'bruno'
import unittest

import algorithms.lists.stack as Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        pass

    def test_stack_fifo_1(self):
        stack = Stack.StackFIFO(Stack.Element(5))
        stack.push(Stack.Element(4))
        stack.push(Stack.Element(3))
        stack.push(Stack.Element(2))
        stack.push(Stack.Element(1))
        self.assertEqual(5, stack.pop())
        self.assertEqual(4, stack.pop())
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())
        self.assertEqual(True, stack.empty())

    def test_stack_fifo_2(self):
        stack = Stack.StackFIFO(Stack.Element(0))
        for i in range(1, 11):
            stack.push(Stack.Element(i))

        for i in range(11):
            self.assertEqual(i, stack.pop())
        self.assertEqual(True, stack.empty())

    def test_stack_fifo_3(self):
        stack = Stack.StackFIFO(Stack.Element(0))
        for i in range(1, 201):
            stack.push(Stack.Element(i))

        for i in range(201):
            self.assertEqual(i, stack.pop())
        self.assertEqual(True, stack.empty())

    def test_stack_fifo_4(self):
        stack = Stack.StackFIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))

        self.assertEqual(500, stack.count())

    def test_stack_fifo_5(self):
        stack = Stack.StackFIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        for i in range(100):
            self.assertEqual(i, stack.pop())
        self.assertEqual(400, stack.count())

    def test_stack_fifo_6(self):
        stack = Stack.StackFIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        for i in range(300):
            self.assertEqual(i, stack.pop())
        self.assertEqual(200, stack.count())

    def test_stack_fifo_7(self):
        stack = Stack.StackFIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        for i in range(350):
            self.assertEqual(i, stack.pop())
        self.assertEqual(150, stack.count())

    def test_stack_fifo_8(self):
        stack = Stack.StackFIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        for i in range(300):
            self.assertEqual(i, stack.pop())
        self.assertEqual(200, stack.count())

        for i in range(300, 500):
            self.assertEqual(i, stack.pop())
        self.assertEqual(0, stack.count())

    def test_stack_fifo_9(self):
        stack = Stack.StackFIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        for i in range(350):
            self.assertEqual(i, stack.pop())
        self.assertEqual(150, stack.count())

    def test_stack_fifo_10(self):
        stack = Stack.StackFIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        for i in range(500):
            self.assertEqual(i, stack.pop())
        self.assertEqual(0, stack.count())

        self.assertEqual(None, stack.pop())

    def test_stack_lifo_1(self):
        stack = Stack.StackLIFO(Stack.Element(5))
        stack.push(Stack.Element(4))
        stack.push(Stack.Element(3))
        stack.push(Stack.Element(2))
        stack.push(Stack.Element(1))
        self.assertEqual(1, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(3, stack.pop())
        self.assertEqual(4, stack.pop())
        self.assertEqual(5, stack.pop())
        self.assertEqual(True, stack.empty())

    def test_stack_lifo_2(self):
        stack = Stack.StackLIFO(Stack.Element(0))
        for i in range(1, 11):
            stack.push(Stack.Element(i))

        indexes = range(11)

        for i in indexes[::-1]:
            self.assertEqual(i, stack.pop())
        self.assertEqual(True, stack.empty())

    def test_stack_lifo_3(self):
        stack = Stack.StackLIFO(Stack.Element(0))
        for i in range(1, 201):
            stack.push(Stack.Element(i))

        indexes = range(201)

        for i in indexes[::-1]:
            self.assertEqual(i, stack.pop())
        self.assertEqual(True, stack.empty())

    def test_stack_lifo_4(self):
        stack = Stack.StackLIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))

        self.assertEqual(500, stack.count())

    def test_stack_lifo_5(self):
        stack = Stack.StackLIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        indexes = range(400, 500)

        for i in indexes[::-1]:
            self.assertEqual(i, stack.pop())
        self.assertEqual(400, stack.count())

    def test_stack_lifo_6(self):
        stack = Stack.StackLIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        indexes = range(200, 500)

        for i in indexes[::-1]:
            self.assertEqual(i, stack.pop())
        self.assertEqual(200, stack.count())

    def test_stack_lifo_7(self):
        stack = Stack.StackLIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        indexes = range(150, 500)

        for i in indexes[::-1]:
            self.assertEqual(i, stack.pop())
        self.assertEqual(150, stack.count())

    def test_stack_lifo_8(self):
        stack = Stack.StackLIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        indexes = range(200, 500)

        for i in indexes[::-1]:
            self.assertEqual(i, stack.pop())
        self.assertEqual(200, stack.count())

        indexes = range(200)

        for i in indexes[::-1]:
            self.assertEqual(i, stack.pop())
        self.assertEqual(0, stack.count())

    def test_stack_lifo_9(self):
        stack = Stack.StackLIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        indexes = range(150, 500)

        for i in indexes[::-1]:
            self.assertEqual(i, stack.pop())
        self.assertEqual(150, stack.count())

    def test_stack_lifo_10(self):
        stack = Stack.StackLIFO(Stack.Element(0))
        for i in range(1, 500):
            stack.push(Stack.Element(i))
        self.assertEqual(500, stack.count())

        indexes = range(500)

        for i in indexes[::-1]:
            self.assertEqual(i, stack.pop())
        self.assertEqual(0, stack.count())

        self.assertEqual(None, stack.pop())