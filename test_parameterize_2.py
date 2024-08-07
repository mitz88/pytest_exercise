#! /bin/python3

## test_parametrize_0.py
## Pytest to demonstrate how double parametrized inputs behave on a pytest test.It makes a 
##      cartesian product of the two combinations of both parameterized inputs
## Author: Mitesh Kumar
## Date  : 8-Aug-2024


import pytest

# A simple square function
def square(num):
        return num * num


@pytest.mark.parametrize("num", [2,4,6,8,10])
def test_square(num):
        result = square(num)
        assert result == num ** 2

