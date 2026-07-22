from gaemi_trim import chunks_list, gaemi_trim, trim_whole_chunks
from gaemi_brute import gaemi_middle


def test_chunks_list():
    assert chunks_list("111221") == ["111", "22", "1"]
    assert chunks_list("312211") == ["3", "1", "22", "11"]


def test_trim_whole_chunks():
    assert trim_whole_chunks("112132123", 5) == "21321"


def test_gaemi_trim_1():
    assert gaemi_trim(1) == -1


def test_gaemi_trim_5():
    assert gaemi_trim(5) == 12


def test_gaemi_trim_8():
    assert gaemi_trim(8) == 21


def test_gaemi_trim_12():
    assert gaemi_trim(12) == 11


def test_gaemi_trim_15():
    assert gaemi_trim(15) == gaemi_middle(15)


def test_gaemi_trim_18():
    assert gaemi_trim(18) == gaemi_middle(18)


def test_gaemi_trim_32():
    assert gaemi_trim(30) == gaemi_middle(30)


def test_gaemi_trim_99():
    assert gaemi_trim(99)
