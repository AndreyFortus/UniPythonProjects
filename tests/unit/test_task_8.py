from unittest import mock

import numpy as np
import pytest

from lab_8.task_8_2 import figure
from lab_8.task_8_3 import numbers
from lab_8.task_8_4 import check_num
from lab_8.task_8_6 import year_check
from lab_8.task_8_9 import money
from lab_8.task_8_10 import chess
from lab_8.task_8_11 import decimal_convert, binary_convert


def test_binary_convert():
    actual = binary_convert(2019)
    expected = '11111100011'
    assert actual == expected


def test_decimal_convert():
    actual = decimal_convert(11111100011)
    expected = 2019
    assert actual == expected


@pytest.mark.parametrize('input_param, expected', [(4, '4 is even'), (5, '5 is odd')])
def test_check_num(input_param, expected):
    with mock.patch('builtins.input', return_value=input_param):
        actual = check_num()
        expected = expected
        assert actual == expected


def test_figure_positive():
    actual = figure(3)
    expected = 'The figure with 3 sides is triangle'
    assert actual == expected


def test_figure_negative():
    actual = figure(8)
    expected = 'for the correct operation of the program, the number of sides must be 3-6'
    assert actual == expected


def test_numbers():
    input_data = np.arange(1, 10, 1)
    actual = numbers(input_data)
    expected = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
    assert actual == expected


def test_year_check_ord():
    actual = year_check(2012)
    expected = 'Leap year'
    assert actual == expected


def test_year_check_leap():
    actual = year_check(2037)
    expected = 'Ordinary year'
    assert actual == expected


@pytest.mark.parametrize('input_param, expected',
                         [(200, f'Lesia Ukrainka is depicted on 200 hryvnias'),
                          (777, 'Nominal not found. Try another')])
def test_money(input_param, expected):
    with mock.patch('builtins.input', return_value=input_param):
        actual = money()
        expected = f'{expected}'
        assert actual == expected


@pytest.mark.parametrize('input_param, expected',
                         [('f7', 'square is white'), ('d4', 'square is black'), ('abra_cadabra', 'Out of chess field')])
def test_chess(input_param, expected):
    with mock.patch('builtins.input', return_value=input_param):
        actual = chess()
        expected = f'{expected}'
        assert actual == expected
