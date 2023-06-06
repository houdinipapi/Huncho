# Testing the functionality of seasons.py
import pytest
from seasons import print_age_in_mins


def test_seasons():
    assert (
        print_age_in_mins("525600")
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
