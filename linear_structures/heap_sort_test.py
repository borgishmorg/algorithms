import pytest
from .heap_sort import heap_sort
from ..linear_time_sorts.test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=TEST_ARRAYS,
)
def test_heap_sort(array: list, sorted_array: list):
    assert heap_sort(array) == [
        *reversed(sorted_array)
    ]  # heap_sort sorts in descending order
