from lab_6.task_6_1 import total_count


def test_total_count():
    actual = total_count(0)
    expected = f'Total of all numbers: 12149.0'
    assert actual == expected
