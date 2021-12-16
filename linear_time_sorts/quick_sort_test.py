import pytest
from .quick_sort import quick_sort
from .test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=TEST_ARRAYS,
)
def test_quick_sort(array: list, sorted_array: list):
    assert quick_sort(array) == sorted_array
