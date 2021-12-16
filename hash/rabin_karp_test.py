import pytest
from .rabin_karp import rabin_karp


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
def test_rabin_karp(a: str, x: str):
    assert rabin_karp(a, x) == a.find(x)
