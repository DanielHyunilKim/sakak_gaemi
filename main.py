def gaemi(n: int, L: int = 1) -> int:

    if n < 1:
        return -1

    current_str = str(L)

    for _ in range(1, n):
        next_str = ""
        count = 0
        tracking_c = ""

        for c in current_str:
            if tracking_c == "":
                tracking_c = c
            elif tracking_c != c:
                next_str += str(count) + tracking_c
                tracking_c = c
                count = 0
            count += 1
        
        next_str += str(count) + tracking_c
        current_str = next_str

    return int(next_str)
