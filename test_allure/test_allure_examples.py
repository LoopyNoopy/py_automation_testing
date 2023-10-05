import pytest

#https://allurereport.org/docs/frameworks/python/pytest/

@pytest.mark.parametrize("num1, num2, expected", [(1, 2, 3), (2, 3, 5), (5, 5, 10)])
def test_addition(num1, num2, expected):
    result = num1 + num2
    assert result == expected

@pytest.mark.slow
def test_slow_operation():
    # Your slow test code here
    pass
