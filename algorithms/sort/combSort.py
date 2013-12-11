__author__ = 'bruno'


def comb_sort(unordered):
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