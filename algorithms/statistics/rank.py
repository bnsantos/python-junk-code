__author__ = 'bruno'


def rank(unsorted_list, value):
    pos = 0
    for val in unsorted_list:
        if val <= value:
            pos += 1
    return pos


def partition(unsorted_list, value):
    lesser = []
    greater = []
    for val in unsorted_list:
        if val < value:
            lesser.append(val)
        else:
            greater.append(val)
    final_list = lesser + [value] + greater
    return final_list