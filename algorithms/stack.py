__author__ = 'bruno'


class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next_elem):
        self.next = next_elem


#FIFO - last in first out
class StackFIFO:
    def __init__(self, elem):
        self.first = elem
        self.last = elem
        self.elements = 1

    def pop(self):
        if self.elements > 0:
            self.elements -= 1
            pop = self.first
            self.first = self.first.next
            return pop.value
        else:
            return None

    def push(self, elem):
        self.elements += 1
        self.last.set_next(elem)
        self.last = elem

    def count(self):
        return self.elements

    def empty(self):
        return self.elements==0