__author__ = 'bruno'


class IntNode(object):
    def __init__(self, children_left, children_right, value):
        self.left = children_left
        self.right = children_right
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


class BinaryTree(object):
    def __init__(self, root):
        self.root = root

    def add_node(self, node):
        current = self.root
        is_leaf = False
        while not is_leaf:
            if current.value > node.get_value():
                #go to left
                if current.get_left() is None:
                    is_leaf = True
                    current.set_left(node)
                else:
                    current = current.get_left()
            else:
                #go to right
                if current.get_right() is None:
                    is_leaf = True
                    current.set_right(node)
                else:
                    current = current.get_right()

    def find_node(self, value):
        current = self.root
        while current:
            if current.get_value() > value:
                #go to left
                current = current.get_left()
            elif current.get_value() < value:
                #go to right
                current = current.get_right()
            else:
                return current.get_value()
        return None

    @staticmethod
    def find_min(node):
        current = node
        while current.get_left():
            current = current.get_left()
        return current

    def delete_node(self, node, root=None):
        if root is None:
            root = self.root
        parent = root
        current = root
        found = False
        while not found:
            if current is None:
                return False
            if current.get_value() > node.get_value():
                #go to left
                parent = current
                current = current.get_left()
            elif current.get_value() < node.get_value():
                #go to right
                parent = current
                current = current.get_right()
            else:
                found = True
        if current.get_left() is None and current.get_right() is None:
            if parent.get_left() == current:
                parent.set_left(None)
            else:
                parent.set_right(None)
            return True
        elif current.get_left() is None and current.get_right() is not None:
            if parent.get_left() == current:
                parent.set_left(current.get_right())
            else:
                parent.set_right(current.get_right())
            return True
        elif current.get_left() is not None and current.get_right() is None:
            if parent.get_left() == current:
                parent.set_left(current.get_left())
            else:
                parent.set_right(current.get_left())
            return True
        else:
            successor = BinaryTree.find_min(current.get_right())
            current.set_value(successor.get_value())
            return self.delete_node(successor, current.get_right())
            return True