__author__ = 'bruno'


def comb_sort(unordered):
    """
        Worst case Big Omega(n^2)
        Best case O(n)
        Avg case Big Omega(n^2/2^P) - P is the number of increments
        Worst case space O(1)
    """
    gap = len(unordered)
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.25))   # minimum gap is 1
        swapped = False
        for i in range(len(unordered)-gap):
            if unordered[i] > unordered[i+gap]:
                unordered[i], unordered[i+gap] = unordered[i+gap], unordered[i]
                swapped = True
    return unordered