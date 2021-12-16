import pytest
from .hoar_sort import hoar_sort
from .test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=TEST_ARRAYS,
)
def test_hoar_sort(array: list, sorted_array: list):
    assert hoar_sort(array) == sorted_array
