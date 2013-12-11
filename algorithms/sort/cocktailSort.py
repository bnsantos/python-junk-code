__author__ = 'bruno'


def cocktail_sort(unordered):
    """
        Worst case O(n^2)
        Best case O(n)
        Avg case O(n^2)
        Worst case space O(1)
    """
    length = len(unordered)-1
    swapped = True
    while swapped:
        for indices in (range(length), reversed(range(length))):
            swapped = False
            for i in indices:
                if unordered[i] > unordered[i+1]:
                    unordered[i], unordered[i+1] = unordered[i+1], unordered[i]
                    swapped = True
            if not swapped:
                break
    return unordered
