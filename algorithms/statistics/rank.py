__author__ = 'bruno'


def rank(unsorted_list, value):
    pos = 0
    for val in unsorted_list:
        if val <= value:
            pos += 1
    return pos
