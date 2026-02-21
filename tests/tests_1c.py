import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_two_elements():
    assert max_subarray_sum([1, -2]) == 1