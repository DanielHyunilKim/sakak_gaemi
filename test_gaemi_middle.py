from main import gaemi_middle


def test_gaemi_middle_1():
    assert gaemi_middle(1) == -1

def test_gaemi_middle_5():
    assert gaemi_middle(5) == 12

def test_gaemi_middle_8():
    assert gaemi_middle(8) == 21

def test_gaemi_middle_12():
    assert gaemi_middle(12) == 11
