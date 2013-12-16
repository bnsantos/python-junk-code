__author__ = 'bruno'


def find_maximum(values):
    if len(values) > 0:
        maximum = values[0]
        for item in values:
            if item > maximum:
                maximum = item

        return maximum