from lab_6.task_6_1 import total_count
from lab_6.task_6_3 import create_list


def test_total_count():
    actual = total_count(0)
    expected = f'Total of all numbers: 12149.0'
    assert actual == expected


def test_create_list():
    actual = create_list()
    expected = [['In Python you can diving into data science and math\n',
                 'In Python you can speeding up and automating your workflow\n',
                 'In Python you can building embedded systems and robots']]
    assert actual == expected
