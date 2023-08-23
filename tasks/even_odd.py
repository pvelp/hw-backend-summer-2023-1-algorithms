__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even = sum([x for x in arr if x % 2 == 0])
    odd = sum([x for x in arr if x % 2 != 0])
    return even / odd if odd != 0 else 0
