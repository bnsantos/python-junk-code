__author__ = 'bruno'


def get_abacus_line(n=0):
    line = '|00000*****|'
    return line[:-1-n] + '   ' + line[-1-n:]


def generate_abacus(value):
    abacus = []
    factor = 1000000000
    while factor >= 1:
        if value >= factor:
            abacus.append(get_abacus_line(int(value/factor)))
            value -= int(value / factor) * factor
        else:
            abacus.append(get_abacus_line())
        factor /= 10
    return abacus


def print_abacus(abacus):
    for line in abacus:
        print line