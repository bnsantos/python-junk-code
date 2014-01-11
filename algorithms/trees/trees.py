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
            successor = BinarySearchTree.find_min(current.get_right())
            current.set_value(successor.get_value())
            return self.delete_node(successor, current.get_right())
            return True

    def print_pre_order(self):
        to_visit = [self.root]
        pre_order = []
        while to_visit:
            current = to_visit.pop()
            pre_order.append(current.get_value())
            if current.get_right():
                to_visit.append(current.get_right())
            if current.get_left():
                to_visit.append(current.get_left())
        return pre_order

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

    def print_post_order(self):
        current = self.root
        parent_stack = []
        post_order = []
        last_node_visited = None
        while parent_stack or current is not None:
            if current:
                parent_stack.append(current)
                current = current.get_left()
            else:
                peek_node = parent_stack[len(parent_stack)-1]
                if peek_node.get_right() and last_node_visited != peek_node.get_right():
                    current = peek_node.get_right()
                else:
                    visited = parent_stack.pop()
                    post_order.append(visited.get_value())
                    last_node_visited = peek_node
        return post_order

    def lowest_common_ancestor(self, node1_value, node2_value):
        current = self.root

        while current:
            if current.get_value() > node1_value and current.get_value() > node2_value:
                current = current.get_left()
            elif current.get_value() < node1_value and current.get_value() < node2_value:
                current = current.get_right()
            else:
                return current.get_value()
        return None


class IntNode(object):
    def __init__(self, children, value):
        self.children = children
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_child(self, index):
        return self.children[index]

    def get_children(self):
        return self.children

    def get_child_num(self):
        return len(self.children)

    def add_child(self, child):
        self.children.append(child)


class Tree(object):
    def __init__(self, node):
        self.root = node

    def breadth_first_search(self, value):
        to_visit = [self.root]
        while to_visit:
            current = to_visit.pop()
            if current.get_value() == value:
                return True
            else:
                children = current.get_children()
                if children:
                    children = children[::-1]
                    to_visit = children + to_visit
        return False

    def depth_first_search(self, value):
        to_visit = [self.root]
        while to_visit:
            current = to_visit.pop()
            if current.get_value() == value:
                return True
            else:
                children = current.get_children()
                if children:
                    children = children[::-1]
                    to_visit = to_visit + children
        return False

    def get_height(self):
        to_visit = [[self.root, 1]]
        max_height = 0
        while to_visit:
            current = to_visit.pop()
            children = current[0].get_children()
            if children:
                children = children[::-1]
                children_to_visit = []
                for child in children:
                    if max_height < current[1]+1:
                        max_height = current[1]+1
                    children_to_visit.append([child, current[1]+1])
                to_visit = to_visit + children_to_visit
        return max_height