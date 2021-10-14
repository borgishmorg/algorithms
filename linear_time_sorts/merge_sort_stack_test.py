import pytest
from .merge_sort_stack import merge_sort_stack
from .test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=filter(lambda a: len(a[0]) < 1e5, TEST_ARRAYS),
)
def test_merge_sort_stack(array: list, sorted_array: list):
    assert merge_sort_stack(array) == sorted_array
