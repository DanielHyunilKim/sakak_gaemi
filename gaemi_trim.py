from gaemi_brute import next_lns


def gaemi_trim(n: int, L: int = 1) -> int:
    """
    n: nth sequence of Look and Say
    L: starting sequence at n = 1

    Returns computed Look and Say sequence
    """

    if n < 4 or n > 99:
        return -1

    current = str(L)

    for _ in range(1, n):
        next_sequence = next_lns(current)
        next_sequence = trim_whole_chunks(next_sequence, 100)

        current = next_sequence

    middle = len(current) // 2

    return int(current[middle - 1 : middle + 1])


def trim_whole_chunks(sequence: str, max_length: int) -> str:
    """Trim roughly equally from both ends without splitting a chunk."""
    excess = len(sequence) - max_length
    if excess <= 0:
        return sequence

    chunks = chunks_list(sequence)
    left_target = (excess + 1) // 2
    right_target = excess // 2
    left = right = 0

    while left < len(chunks) and left_target > 0:
        left_target -= len(chunks[left])
        left += 1

    while right < len(chunks) - left and right_target > 0:
        right_target -= len(chunks[-right - 1])
        right += 1

    return "".join(chunks[left : len(chunks) - right])


def chunks_list(sequence: str) -> list:
    """
    sequence: string of a Look and Say sequence

    Returns a list of the sequence by chunks.

    Ex. sequence = ["111221"] -> returns ["111", "22", "1"]
    """

    res = []
    curr_chunk = ""
    tracking_c = ""

    for c in sequence:
        if tracking_c == "":
            tracking_c = c
        elif tracking_c != c:
            res.append(curr_chunk)
            curr_chunk = ""
            tracking_c = c
        curr_chunk += tracking_c

    res.append(curr_chunk)

    return res
