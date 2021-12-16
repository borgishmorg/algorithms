import pytest
from .count_sort import count_sort
from .test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=filter(lambda arr: not arr[0] or type(arr[0][0]) is int, TEST_ARRAYS),
)
def test_count_sort(array: list, sorted_array: list):
    assert count_sort(array) == sorted_array
