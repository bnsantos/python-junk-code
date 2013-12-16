__author__ = 'bruno'


def find_minimum(values):
    if len(values) > 0:
        minimum = values[0]
        for item in values:
            if item < minimum:
                minimum = item

        return minimum