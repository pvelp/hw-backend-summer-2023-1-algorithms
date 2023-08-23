from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    res = []
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    for i in range(len_arr1 if len_arr1 < len_arr2 else len_arr2):
        res.append((arr1[i], arr2[i]))
    return res
