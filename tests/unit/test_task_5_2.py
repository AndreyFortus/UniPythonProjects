from task_5_2 import digits_counter


def test_counter():
    input_param = 25346
    actual = digits_counter(input_param)
    expected = 5
    assert actual == expected
