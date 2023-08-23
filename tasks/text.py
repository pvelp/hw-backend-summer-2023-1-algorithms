from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    delimiters = [';', ',', ':', '.', '|', '\n', '\t', '-']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    tmp = text.split()
    for delim in delimiters:
        tmp = ' '.join(tmp).split(delim)
    for digit in digits:
        tmp = ' '.join(tmp).split(digit)
    new_str = tmp[0]

    if len(new_str) != 0:
        minimum = min(new_str.split(), key=len)
        maximum = max(new_str.split(), key=len)
    else:
        maximum, minimum = None, None
    return minimum, maximum
