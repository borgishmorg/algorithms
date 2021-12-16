import pytest
from .quick_sort_stack import quick_sort_stack
from .test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=TEST_ARRAYS,
)
def test_quick_sort_stack(array: list, sorted_array: list):
    assert quick_sort_stack(array) == sorted_array
