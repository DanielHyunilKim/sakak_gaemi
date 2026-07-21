def gaemi(n: int, L: int = 1) -> int:

    if n < 1:
        return -1

    current = str(L)

    for _ in range(1, n):
        next = ""
        count = 0
        tracking_c = ""

        for c in current:
            if tracking_c == "":
                tracking_c = c
            elif tracking_c != c:
                next += str(count) + tracking_c
                tracking_c = c
                count = 0
            count += 1
        
        next += str(count) + tracking_c
        current = next

    return int(next)


def gaemi_middle(n: int, L: int = 1) -> int:

    if n < 3 or n > 100:
        return -1

    gaemi_str = str(gaemi(n, L))
    gaemi_len = len(gaemi_str)
    middle = gaemi_len // 2

    return int(gaemi_str[middle - 1 : middle + 1])