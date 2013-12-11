__author__ = 'bruno'


def insertion_sort(unordered):
    for i in range(1, len(unordered)):
        tmp = unordered[i]
        k = i
        while k > 0 and tmp < unordered[k-1]:
            unordered[k] = unordered[k-1]
            k -= 1
        unordered[k] = tmp
    return unordered
