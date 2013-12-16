__author__ = 'bruno'


def get_mean(values):
    total = 0
    for item in values:
        total += item
    return total/len(values)