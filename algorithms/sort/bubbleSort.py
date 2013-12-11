__author__ = 'bruno'


def bubble(unsorted):
    length = len(unsorted)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(length-1):
            if unsorted[i] > unsorted[i+1]:
                is_sorted = False
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]

    return unsorted