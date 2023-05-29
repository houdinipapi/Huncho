import twttr


def test_shorten_no_vowels():
    word = "PYTHN"
    expected_output = "PYTHN"
    assert twttr.shorten(word) == expected_output


def test_shorten_all_vowels():
    word = "aeiou"
    expected_output = ""
    assert twttr.shorten(word) == expected_output


def test_shorten_mixed_vowels_and_consonants():
    word = "Hello"
    expected_output = "Hll"
    assert twttr.shorten(word) == expected_output


def test_shorten_empty_string():
    word = ""
    expected_output = ""
    assert twttr.shorten(word) == expected_output


def test_shorten_uppercase_and_lowercase():
    word = "InTeRvIeW"
    expected_output = "nTRvW"
    assert twttr.shorten(word) == expected_output


def test_omitting_numbers():
    word = "p3psi"
    expected_output = "p3ps"
    assert twttr.shorten(word) == expected_output


def test_omitting_punctuation():
    word = "hand.driven"
    expected_output = "hnd.drvn"
    assert twttr.shorten(word) == expected_output
