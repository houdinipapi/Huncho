import fuel
import pytest


def test_convert_valid_fraction():
    assert fuel.convert("3/4") == 75


def test_convert_invalid_fraction():
    fraction = "5/0"
    with pytest.raises(ZeroDivisionError):
        fuel.convert(fraction)


def test_convert_non_integer_fraction():
    fraction = "2.5/3"
    with pytest.raises(ValueError):
        fuel.convert(fraction)


def test_gauge_low_percentage():
    assert fuel.gauge(1) == "E"


def test_gauge_high_percentage():
    assert fuel.gauge(99) == "F"


def test_gauge_mid_percentage():
    assert fuel.gauge(50) == "50%"
