import pytest
from .knuth_morris_pratt import knuth_morris_pratt


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
def test_knuth_morris_pratt(a: str, x: str):
    assert knuth_morris_pratt(a, x) == a.find(x)
