__author__ = 'bruno'


class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next_elem):
        self.next = next_elem


class LinkedList:
    def __init__(self, elem):
        self.head = elem
        self.tail = elem
        self.elements = 1

    def add(self, elem):
        if self.elements == 1:
            self.head.next = elem
            self.tail = elem
        else:
            self.tail.next = elem
            self.tail = elem
        self.elements += 1

    def remove(self, index):
        if index < self.elements:
            i = 0
            previous_elem = self.head
            while i < index - 1 and previous_elem:
                previous_elem = previous_elem.next
                i += 1
            if previous_elem:
                if previous_elem == self.head:
                    self.head, self.tail = previous_elem.next, previous_elem.next
                elif previous_elem.next == self.tail:
                    self.tail = previous_elem
                else:
                    previous_elem.next = previous_elem.next.next
                self.elements -= 1
                return True
        return False

    def find_m_to_last_element(self, m):
        if m > self.elements:
            return False
        else:
            i = 1
            current = self.head
            while i < m:
                if current.next:
                    current = current.next
                    i += 1
                else:
                    return False

            m_behind = self.head
            while current.next:
                current = current.next
                m_behind = m_behind.next

            return m_behind.value

    def empty(self):
        return self.elements == 0

    def count(self):
        return self.elements