#! /bin/python3

## test_parametrize_1.py
## This is a simle test demonstrating how two parametrized inputs are given to a pytest test.
## Author: Mitesh Kumar
## Date  : 7-Aug-2024


import pytest

# A simple multiply function
def square(num):
        return num * num


@pytest.mark.parametrize("x,y", [(2,4),(4,16),(6,36),(8,64),(10,100)])
def test_square(x,y):
        result = square(x)
        assert result == y

