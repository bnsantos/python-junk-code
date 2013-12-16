__author__ = 'bruno'
import maximum as Maximum
import minimum as Minimum


def find_midpoint(values):
    maximum = Maximum.find_maximum(values)
    minimum = Minimum.find_minimum(values)
    return (maximum+minimum)/2

