# Testing working.py
import pytest
from working import convert


def test_colon():
    assert convert("12 AM to 6 AM") == "00:00 to 06:00"
    assert convert("12 PM to 6 PM") == "12:00 to 18:00"
    assert convert("12:01 AM to 6:59 AM") == "00:01 to 06:59"
    assert convert("12:30 PM to 6:03 PM") == "12:30 to 18:03"


def test_user_input():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
