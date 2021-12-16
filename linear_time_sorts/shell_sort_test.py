import pytest
from .shell_sort import shell_sort
from .test_arrays import TEST_ARRAYS


@pytest.mark.parametrize(
    argnames="array, sorted_array",
    argvalues=TEST_ARRAYS,
)
def test_shell_sort(array: list, sorted_array: list):
    assert shell_sort(array) == sorted_array
