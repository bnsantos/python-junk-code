__author__ = 'bruno'


def get_char_key(telephone_key, place):
    if telephone_key == '0' or telephone_key == '1':
        return ''
    if telephone_key == '2':
        return 'ABC'[place]
    if telephone_key == '3':
        return 'DEF'[place]
    if telephone_key == '4':
        return 'GHI'[place]
    if telephone_key == '5':
        return 'JKL'[place]
    if telephone_key == '6':
        return 'MNO'[place]
    if telephone_key == '7':
        return 'PRS'[place]
    if telephone_key == '8':
        return 'TUV'[place]
    if telephone_key == '9':
        return 'WXY'[place]


def print_telephone_words_recursive(telephone):
    phone_words = []
    current = ''
    telephone_words_recursive(telephone, 0, phone_words, current)
    return phone_words


def telephone_words_recursive(telephone, current_digit, phone_words, current_word):
    if current_digit == len(telephone):
        phone_words.append(current_word)
        return
    i = 0
    while i < 3:
        current_word += get_char_key(telephone[current_digit], i)
        telephone_words_recursive(telephone, current_digit + 1, phone_words, current_word)
        current_word = current_word[:-1]
        if telephone[current_digit] == '0' or telephone[current_digit] == '1':
            return
        i += 1