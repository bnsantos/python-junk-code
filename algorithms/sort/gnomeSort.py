__author__ = 'bruno'


def gnome_sort(unordered):
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