import pytest
from .boyer_moore import boyer_moore


@pytest.mark.parametrize(
    "a, x",
    [
        ["ssdijhadiusfyihgdsaoin hi", "sdf"],
        ["abcsgassgasasags", "abc"],
        ["sgassgasabcasags", "abc"],
        ["sgassgasasagsabc", "abc"],
        ["AABAACAADAABAABA", "AABA"],
        ["THIS IS A TEST TEXT", "TEST"],
    ],
)
def test_boyer_moore(a: str, x: str):
    assert boyer_moore(a, x) == a.find(x)
