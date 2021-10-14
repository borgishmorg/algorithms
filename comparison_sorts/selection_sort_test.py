import pytest
from .selection_sort import selection_sort
from .test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=TEST_ARRAYS,
)
def test_selection_sort(array: list, sorted_array: list):
    selection_sort(array)
    assert array == sorted_array
