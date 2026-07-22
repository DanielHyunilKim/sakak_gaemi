from gaemi_conway import element_digit, element_length, gaemi_conway, sequence_digit
from gaemi_brute import gaemi_middle


def test_element_length_base_generation():
    assert element_length("Hf", 0) == 5


def test_element_length_after_decay():
    assert element_length("He", 1) == 38


def test_element_digit_base_generation():
    assert element_digit("Hf", 0, 4) == "2"


def test_element_digit_after_decay():
    assert element_digit("He", 1, 6) == "3"


def test_sequence_digit_base_generation():
    assert sequence_digit(("Hf", "Sn"), 0, 5) == "1"


def test_sequence_digit_after_decay():
    assert sequence_digit(("Hf", "Sn"), 1, 9) == "3"


def test_gaemi_conway_1():
    assert gaemi_conway(1) == -1


def test_gaemi_conway_5():
    assert gaemi_conway(5) == 12


def test_gaemi_conway_8():
    assert gaemi_conway(8) == 21


def test_gaemi_conway_12():
    assert gaemi_conway(12) == 11


def test_gaemi_conway_15():
    assert gaemi_conway(15) == gaemi_middle(15)


def test_gaemi_conway_18():
    assert gaemi_conway(18) == gaemi_middle(18)


def test_gaemi_conway_32():
    assert gaemi_conway(30) == gaemi_middle(30)


def test_gaemi_conway_99():
    assert gaemi_conway(99)
