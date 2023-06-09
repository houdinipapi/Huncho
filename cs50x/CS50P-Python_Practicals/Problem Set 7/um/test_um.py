# Testing the count() in um.py
from um import count


def test_count():
    assert count("hello, um, world") == 1
    assert count("yummy") == 0
    assert count("Um, um, um") == 3
    assert count("The quick brown fox jumps over the lazy dog") == 0


if __name__ == "__main":
    test_count()
