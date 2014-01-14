__author__ = 'bruno'


def remove_pattern(string, pattern):
    if string is None or pattern is None:
        return None
    if type(string) != type(str()) or type(pattern) != type(str()):
        return None
    final_string = ''
    for letter in string:
        if letter not in pattern:
            final_string += letter

    return final_string
