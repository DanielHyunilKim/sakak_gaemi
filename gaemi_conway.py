from functools import cache

from conway import ATOMS, BASE_ATOMS, BASE_TERM_NUMBER, DECAYS
from gaemi_brute import gaemi_middle


def gaemi_conway(n: int, L: int = 1) -> int:
    """
    n: nth sequence of Look and Say
    L: starting sequence at n = 1

    Returns computed middle 2 digits of computed Look and Say sequence
    """

    if n < 4 or n > 99 or L != 1:
        return -1

    if n < BASE_TERM_NUMBER:
        return gaemi_middle(n)

    generations = n - BASE_TERM_NUMBER
    gaemi_len = sum(element_length(name, generations) for name in BASE_ATOMS)
    middle = gaemi_len // 2
    left = sequence_digit(BASE_ATOMS, generations, middle - 1)
    right = sequence_digit(BASE_ATOMS, generations, middle)

    return int(left + right)


@cache
def element_length(name: str, generations: int) -> int:
    """Returns the length of an element after the given generations."""

    if generations == 0:
        return len(ATOMS[name])

    return sum(
        element_length(child, generations - 1) for child in DECAYS[name]
    )


def sequence_digit(names: tuple, generations: int, index: int) -> str:
    """Returns one digit from a sequence of Conway elements."""

    for name in names:
        length = element_length(name, generations)

        if index < length:
            return element_digit(name, generations, index)

        index -= length

    return ""


def element_digit(name: str, generations: int, index: int) -> str:
    """Returns one digit from an element without expanding all descendants."""

    if generations == 0:
        return ATOMS[name][index]

    for child in DECAYS[name]:
        length = element_length(child, generations - 1)

        if index < length:
            return element_digit(child, generations - 1, index)

        index -= length

    return ""
