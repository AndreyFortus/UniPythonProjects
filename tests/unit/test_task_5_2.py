from lab_5.task_5_2 import digits_counter

from unittest.mock import patch, MagicMock


def test_counter():
    mock_input = MagicMock(return_value=12345)
    with patch('builtins.input', mock_input):
        actual = digits_counter()
    mock_input.assert_called_once_with('Input n value: ')
    expected = 5
    assert actual == expected
