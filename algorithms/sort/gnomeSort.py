__author__ = 'bruno'


def gnome_sort(unordered):
    """
        Worst case O(n^2)
        Best case O(n)
        Avg case O(n^2)
        Worst case space O(1)
    """
    pos = 0
    while True:
        if pos == 0:
            pos += 1
        if pos >= len(unordered):
            break
        if unordered[pos] >= unordered[pos-1]:
            pos += 1
        else:
            unordered[pos-1], unordered[pos] = unordered[pos], unordered[pos-1]
            pos -= 1

    return unordered