from lab_5.task_5_2 import digits_counter, main

from unittest.mock import patch


def test_counter():
    with patch('builtins.input', return_value='25346'):
        actual = main()
    expected = 5
    assert actual == expected
