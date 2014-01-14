__author__ = 'bruno'


def find_first_non_repeated_char(string):
    if string is None or len(string) == 0:
        return None
    letters = {}
    for letter in string:
        if letters.__contains__(letter):
            letters[letter] += 1
        else:
            letters[letter] = 1

    for letter in string:
        if letters[letter] == 1:
            return letter

    return None
