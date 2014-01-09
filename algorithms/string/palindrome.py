__author__ = 'bruno'
import helper.validateInput as ValidateInput
from string import letters
import random


def check_character_palindrome(word):
    if ValidateInput.validate_string_input(word):
        word = word.lower()
        if word == word[::-1]:
            return True

    return False


def check_word_palindrome(word):
    if ValidateInput.validate_string_input(word):
        word = word.lower()
        if word == word[::-1]:
            return True

    return False


def generate_palindrome(length):
    word = ''
    if (length % 2) == 1:
        word = random.choice(letters.lower())
        length -= 1

    i = 0
    while i < length:
        letter = random.choice(letters.lower())
        word = letter + word + letter
        i += 2

    return word