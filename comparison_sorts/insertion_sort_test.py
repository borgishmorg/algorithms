import pytest
from .insertion_sort import insertion_sort
from .test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=TEST_ARRAYS,
)
def test_insertion_sort(array: list, sorted_array: list):
    insertion_sort(array)
    assert array == sorted_array
