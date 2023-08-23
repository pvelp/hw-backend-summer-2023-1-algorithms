__all__ = (
    'is_prime',
)

from math import sqrt


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number == 0 or number == 1:
        return False
    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return True
