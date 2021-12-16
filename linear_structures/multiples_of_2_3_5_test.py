import pytest
from .multiples_of_2_3_5 import multiples_of_2_3_5


def multiple_of_2_3_5(k: int) -> bool:
    if k % 2 != 0 and k % 3 != 0 and k % 5 != 0:
        return False
    while not k % 2:
        k //= 2
    while not k % 3:
        k //= 3
    while not k % 5:
        k //= 5
    return k == 1


def dummy_multiples_of_2_3_5(n: int) -> list:
    k = 1
    res = []
    while len(res) < n:
        while not multiple_of_2_3_5(k):
            k += 1
        res.append(k)
        k += 1
    return res


@pytest.mark.parametrize(
    "n",
    [
        0,
        1,
        2,
        5,
        100,
        500,
    ],
)
def test_multiples_of_2_3_5(n: int):
    assert multiples_of_2_3_5(n) == dummy_multiples_of_2_3_5(n)
