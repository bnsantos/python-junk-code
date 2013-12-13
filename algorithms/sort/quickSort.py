__author__ = 'bruno'


def recursive_sort(unordered):
    if unordered == []:
        return unordered
    return recursive_sort([x for x in unordered[1:] if x < unordered[0]]) + unordered[0:1] + \
           recursive_sort([x for x in unordered[1:] if x >= unordered[0]])

