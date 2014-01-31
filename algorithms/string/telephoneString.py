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


def is_done(digit_indexes):
    for index in digit_indexes:
        if index != 2 and index != -1:
            return False
    return True


def get_word(telephone, digit_indexes):
    word = ''
    i = 0
    while i < len(telephone):
        word += get_char_key(telephone[i], digit_indexes[i])
        i += 1
    return word


def increase_digits(digit_indexes):
    to_carry = True
    i = len(digit_indexes) - 1

    while to_carry and i >= 0:
        if digit_indexes[i] == 2:
            digit_indexes[i] = 0
            i -= 1
        elif digit_indexes[i] == -1:
            i -= 1
        else:
            to_carry = False
            digit_indexes[i] += 1


def print_telephone_words_iterative(telephone):
    phone_words = []
    digit_indexes = []
    for digit in telephone:
        if digit != '0' and digit != '1':
            digit_indexes.append(0)
        else:
            digit_indexes.append(-1)

    done = False
    while not done:
        done = is_done(digit_indexes)
        phone_words.append(get_word(telephone, digit_indexes))
        increase_digits(digit_indexes)
    return phone_words