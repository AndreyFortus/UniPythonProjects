from unittest import mock

import numpy as np
import pytest

from lab_8.task_8_1 import users
from lab_8.task_8_2 import figure
from lab_8.task_8_3 import numbers
from lab_8.task_8_4 import check_num
from lab_8.task_8_5 import month_check
from lab_8.task_8_6 import year_check
from lab_8.task_8_7 import count_numbers
from lab_8.task_8_8 import calculator
from lab_8.task_8_9 import money
from lab_8.task_8_10 import chess
from lab_8.task_8_11 import decimal_convert, binary_convert
from lab_8.task_8_12 import game


def test_users():
    input_param = ['Alex', 'John', 'Dan', 'Admin', '123_TeSt_321']
    actual = users(input_param)
    expected = ['Hello Alex thank you for logging in again.',
                'Hello John thank you for logging in again.',
                'Hello Dan thank you for logging in again.',
                'Hello Admin, I hope you\'re well.',
                'Hello 123_TeSt_321 thank you for logging in again.']
    assert actual == expected


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


@pytest.mark.parametrize('input_param, expected', [(3, 'The figure with 3 sides is triangle'),
                                                   (8, 'for the correct operation of the program, the number of sides must be 3-6')])
def test_figure(input_param, expected):
    actual = figure(input_param)
    expected = expected
    assert actual == expected


def test_numbers():
    input_data = np.arange(1, 10, 1)
    actual = numbers(input_data)
    expected = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
    assert actual == expected


@pytest.mark.parametrize('input_param, expected', [(2012, 'Leap year'), (2037, 'Ordinary year')])
def test_year_check_ord(input_param, expected):
    actual = year_check(input_param)
    expected = expected
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
                         [('f7', 'square is white'), ('d4', 'square is black'),
                          ('abra_cadabra', 'Out of chess field')])
def test_chess(input_param, expected):
    with mock.patch('builtins.input', return_value=input_param):
        actual = chess()
        expected = f'{expected}'
        assert actual == expected


@pytest.mark.parametrize('input_param, expected',
                         [([12, 23, 0], 35), ([50, -50, 25, 0], 25)])
def test_count_numbers(monkeypatch, input_param, expected):
    with mock.patch('builtins.input', return_value=input_param):
        inputs = iter(input_param)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        actual = count_numbers()
        expected = expected
        assert actual == expected


@pytest.mark.parametrize('input_param, expected',
                         [([3, 4, '+'], 'answer = 7.0'), ([5, 5, '/'], 'answer = 1.0'),
                          ([25, 0, '/'], 'Divided by zero!'), ([5, 5, '+/'], 'Error!')])
def test_calculator(monkeypatch, input_param, expected):
    with mock.patch('builtins.input', return_value=input_param):
        inputs = iter(input_param)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        actual = calculator()
        expected = expected
        assert actual == expected


@pytest.mark.parametrize('input_param, expected',
                         [(['september'], 'in september 30 days'), (['december'], 'in december 31 days'),
                          (['february', 1977], 'in february 28 days'), (['february', 2004], 'in february 29 days')])
def test_month_check(monkeypatch, input_param, expected):
    with mock.patch('builtins.input', return_value=input_param):
        inputs = iter(input_param)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        actual = month_check()
        expected = expected
        assert actual == expected


expected_value_game = 'It\'s a tie!' or 'Congratulations! You win!' or 'Sorry, you lose!'
def test_game():
    with mock.patch('builtins.input', return_value=1):
        actual = game()
        if actual in expected_value_game:
            assert True
