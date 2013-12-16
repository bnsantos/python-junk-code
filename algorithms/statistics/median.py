__author__ = 'bruno'
import algorithms.sort.quickSort as QuickSort


def median(values):
    values = QuickSort.iterative_sort(values)
    return values[len(values)/2]