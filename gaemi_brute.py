def gaemi(n: int, L: int = 1) -> str:
    """
    n: nth sequence of Look and Say
    L: starting sequence at n = 1

    Returns computed Look and Say sequence
    """

    if n < 1:
        return ""

    current = str(L)

    for _ in range(1, n):
        next = next_lns(current)
        current = next

    return next


def gaemi_middle(n: int, L: int = 1) -> int:
    """
    n: nth sequence of Look and Say
    L: starting sequence at n = 1

    Returns computed middle 2 digits of computed Look and Say sequence
    """

    if n < 4 or n > 99:
        return -1

    gaemi_str = str(gaemi(n, L))
    gaemi_len = len(gaemi_str)
    middle = gaemi_len // 2

    return int(gaemi_str[middle - 1 : middle + 1])


def next_lns(sequence: str) -> str:
    """
    sequence: string of a Look and Say sequence

    Returns the next Look and Say sequence

    Ex. sequence = ["111221"] -> returns "312211"
    """

    lns = []
    tracking_c = ""
    count = 0

    for c in sequence:
        if tracking_c == "":
            tracking_c = c
        elif tracking_c != c:
            lns.append(str(count))
            lns.append(tracking_c)
            tracking_c = c
            count = 0
        count += 1

    lns.append(str(count))
    lns.append(tracking_c)

    return "".join(lns)