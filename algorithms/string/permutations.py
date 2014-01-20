__author__ = 'bruno'


def permutations(string):
    length = len(string)
    used = [False]*length
    out = ''
    out_array = []
    p(string, used, length, out, out_array)
    return out_array


def p(string, used, length, out, out_array):
    i = 0
    if len(out) == len(string):
        out_array.append(out)
    while i < length:
        if used[i]:
            i += 1
            continue
        out += string[i]
        used[i] = True
        p(string, used, length, out, out_array)
        used[i] = False
        out = out[:-1]
        i += 1
