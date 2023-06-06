# Testing teh functions in jar.py

import pytest
from jar import Jar


def test_jar_init():
    jar = Jar(capacity=10)
    assert jar.capacity == 10

    with pytest.raises(ValueError):
        Jar(capacity=-5)


def test_jar_deposit():
    jar = Jar(capacity=10)
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(3)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(5)


def test_jar_withdraw():
    jar = Jar(capacity=10)
    jar.deposit(7)
    jar.withdraw(3)
    assert jar.size == 4

    jar.withdraw(4)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_jar_str():
    jar = Jar(capacity=6)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"

    jar.withdraw(3)
    assert str(jar) == "🍪🍪"


def test_jar_size():
    jar = Jar(capacity=8)
    assert jar.size == 0

    jar.deposit(5)
    assert jar.size == 5

    jar.withdraw(3)
    assert jar.size == 2


if __name__ == "__main__":
    pytest.main()
