__author__ = 'bruno'
import string


class Caesar:
    def __init__(self):
        self.__letters = string.ascii_uppercase

    def encrypt(self, msg, key=3):
        msg = msg.upper()
        cipher = ''
        for char in msg:
            if char in self.__letters:
                idx = self.__letters.find(char) + key
                if idx >= 26:
                    idx -= 26
                cipher += self.__letters[idx]
        return cipher

    def decrypt(self, msg, key=3):
        pass
