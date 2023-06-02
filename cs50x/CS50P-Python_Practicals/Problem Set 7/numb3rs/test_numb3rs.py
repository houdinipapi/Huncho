#!/usr/bin/python3

"""
- Unit tests for the numb3rs.py file
"""

from numb3rs import validate


def main():
    test_validate()
    test_range()


def test_validate():
    # Validating valid IPv4 addresses
    assert validate("192.168.0.1") == True
    assert validate("172.16.0.0") == True
    assert validate("10.0.0.255") == True

    # Invalid IPv4 addresses
    assert validate("256.0.0.1") == False
    assert validate("192.168.0") == False
    assert validate("192.168.0.1.2") == False


def test_range():
    assert validate(r"1.2.3.255") == True
    assert validate(r"1.2.3.1000") == False
    assert validate(r"512.2.3.255") == False
    assert validate(r"51.520.3.255") == False
    assert validate(r"51.2.300.255") == False


if __name__ == "__main__":
    main()
