__author__ = 'bruno'


def bubble(unsorted):
    """
        Worst case O(n^2)
        Best case O(n)
        Avg case O(n^2)
        Worst case space O(1)
    """
    length = len(unsorted)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(length-1):
            if unsorted[i] > unsorted[i+1]:
                is_sorted = False
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]

    return unsorted