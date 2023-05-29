from plates import is_valid


def test_valid():
    assert is_valid("XY70") == True
    assert is_valid("M") == False
    assert is_valid("NJ6.28") == False
    assert is_valid("verylongstate") == False
    assert is_valid("BBB11B") == False
    assert is_valid("DQ04") == False
    assert is_valid("68GGR") == False
    assert is_valid("97") == False
