__author__ = 'bruno'


def recursive_combinations(string):
    out = []
    combine(string, 0, out, '')
    return out


def combine(string, index, out, current_combination):
    while index < len(string):
        current_combination += string[index]
        out.append(current_combination)
        combine(string, index+1, out, current_combination)
        current_combination = current_combination[:-1]
        index += 1
