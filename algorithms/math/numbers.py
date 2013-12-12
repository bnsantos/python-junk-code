__author__ = 'bruno'


def decimal_to_roman(number):
    uni = [''] + 'I II III IV V VI VII VIII IX'.split()
    dez = [''] + 'X XX XXX XL L LX LXX LXXX XC'.split()
    cen = [''] + 'C CC CCC CD D DI DII DIII IM'.split()
    mil = [''] + 'M MM MMM ~IV ~V ~VI ~VII ~VIII ~IX'.split()

    m = number//1000
    dec = number % 1000
    c = dec//100
    dec %= 100
    d = dec//10
    dec %= 10
    u = dec
    return mil[m]+cen[c]+dez[d]+uni[u]
