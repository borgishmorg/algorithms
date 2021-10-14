import pytest
from .merge_sort import merge_sort
from .test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=TEST_ARRAYS,
)
def test_merge_sort_sort(array: list, sorted_array: list):
    assert merge_sort(array) == sorted_array
