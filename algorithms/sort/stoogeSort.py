__author__ = 'bruno'


def sort(unsorted, i_start=0, i_end=0):
    if len(unsorted) == 0:
        return unsorted
    if unsorted[i_end] < unsorted[i_start]:
        unsorted[i_end], unsorted[i_start] = unsorted[i_start], unsorted[i_end]
    if i_end - i_start + 1 >= 3:
        t = (i_end - i_start + 1) / 3
        sort(unsorted, i_start, i_end-t)
        sort(unsorted, i_start+t, i_end)
        sort(unsorted, i_start, i_end-t)
    return unsorted
