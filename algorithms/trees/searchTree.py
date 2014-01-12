__author__ = 'bruno'


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