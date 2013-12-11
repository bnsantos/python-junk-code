__author__ = 'bruno'


def insertion_sort(unordered):
    """
        Worst case O(n^2)
        Best case O(n) comparisons O(1) swaps
        Avg case O(n^2)
        Worst case space O(n)
    """

    for i in range(1, len(unordered)):
        tmp = unordered[i]
        k = i
        while k > 0 and tmp < unordered[k-1]:
            unordered[k] = unordered[k-1]
            k -= 1
        unordered[k] = tmp
    return unordered
