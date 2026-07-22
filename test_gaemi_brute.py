from gaemi_brute import gaemi, next_lns, gaemi_middle

def test_next_lns():
    assert next_lns("111221") == "312211"
    assert next_lns("312211") == "13112221"

def test_gaemi_2():
    assert gaemi(2) == "11"

def test_gaemi_3():
    assert gaemi(3) == "21"

def test_gaemi_4():
    assert gaemi(4) == "1211"

def test_gaemi_5():
    assert gaemi(5) == "111221"

def test_gaemi_6():
    assert gaemi(6) == "312211"

def test_gaemi_12():
    assert gaemi(12) == "3113112221232112111312211312113211"

def test_gaemi_middle_1():
    assert gaemi_middle(1) == -1

def test_gaemi_middle_5():
    assert gaemi_middle(5) == 12

def test_gaemi_middle_8():
    assert gaemi_middle(8) == 21

def test_gaemi_middle_12():
    assert gaemi_middle(12) == 11

def test_gaemi_middle_15():
    assert gaemi_middle(15) == 21
