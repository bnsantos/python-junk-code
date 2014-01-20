__author__ = 'bruno'


def recursive_permutations(string):
    length = len(string)
    used = [False]*length
    out = ''
    out_array = []
    rec_permutations(string, used, length, out, out_array)
    return out_array


def rec_permutations(string, used, length, out, out_array):
    i = 0
    if len(out) == len(string):
        out_array.append(out)
    while i < length:
        if used[i]:
            i += 1
            continue
        out += string[i]
        used[i] = True
        rec_permutations(string, used, length, out, out_array)
        used[i] = False
        out = out[:-1]
        i += 1
