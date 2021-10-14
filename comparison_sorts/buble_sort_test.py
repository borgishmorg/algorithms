import pytest
from .buble_sort import buble_sort
from .test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=TEST_ARRAYS,
)
def test_buble_sort(array: list, sorted_array: list):
    buble_sort(array)
    assert array == sorted_array
