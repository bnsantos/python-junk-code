__author__ = 'bruno'


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        for div in range(2, number/2):
            if number % div == 0:
                return False

        return True