#! /bin/python3

## test_parametrize_0.py
## This is a simle test demonstrating how parametrized inputs are given to a pytest test.
## Author: Mitesh Kumar
## Date  : 7-Aug-2024


import pytest

# A simple square function
def square(num):
        return num * num


@pytest.mark.parametrize("num", [2,4,6,8,10])
def test_square(num):
        result = square(num)
        assert result == num ** 2

