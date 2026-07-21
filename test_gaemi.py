from main import gaemi


def test_gaemi_2():
    assert gaemi(2) == 11

def test_gaemi_3():
    assert gaemi(3) == 21

def test_gaemi_4():
    assert gaemi(4) == 1211

def test_gaemi_5():
    assert gaemi(5) == 111221

def test_gaemi_6():
    assert gaemi(6) == 312211

def test_gaemi_12():
    assert gaemi(12) == 3113112221232112111312211312113211

