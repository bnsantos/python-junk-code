__author__ = 'bruno'


def sort(unordered):
    """
    worst case O(n^2)
    """
    for i in range(len(unordered)):
        min_index = i
        for j in range(i, len(unordered)):
            if unordered[j] < unordered[min_index]:
                min_index = j

        if min_index != i:
            unordered[i], unordered[min_index] = unordered[min_index], unordered[i]
    return unordered