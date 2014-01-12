__author__ = 'bruno'


class IntBinaryNode(object):
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


class BinarySearchTree(object):
    def __init__(self, root):
        self.root = root

    def heapify_binary_tree(self):
        node_array = []
        BinarySearchTree.traverse(self.root, 0, node_array)

        node_array = sorted(node_array, key=lambda node: node.get_value())

        i = 0
        size = len(node_array)
        self.root = node_array[0]
        while i < size:
            left = 2*i + 1
            right = left + 1
            if left >= size:
                node_array[i].set_left(None)
            else:
                node_array[i].set_left(node_array[left])
            if right >= size:
                node_array[i].set_right(None)
            else:
                node_array[i].set_right(node_array[right])
            i += 1

        return True

    @staticmethod
    def traverse(node, count, node_array):
        if node is None:
            return count
        if node_array is not None:
            node_array.append(node)
        count += 1
        count = BinarySearchTree.traverse(node.get_left(), count, node_array)
        count = BinarySearchTree.traverse(node.get_right(), count, node_array)
        return count

    def print_in_order(self):
        parent_stack = []
        to_visit = [self.root]
        in_order = []
        while to_visit or parent_stack:
            if to_visit:
                current = to_visit.pop()
                while current.get_left():
                    parent_stack.append(current)
                    current = current.get_left()
            else:
                current = parent_stack.pop()

            in_order.append(current.get_value())
            if current.get_right():
                to_visit.append(current.get_right())
        return in_order
