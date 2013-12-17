__author__ = 'bruno'


def mode(values):
    counts = {}
    max_value = -1
    max_key = None
    for v in values:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
        if counts[v] > max_value:
            max_value = counts[v]
            max_key = v

    return max_key
