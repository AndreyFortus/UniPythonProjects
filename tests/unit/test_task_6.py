from lab_6.task_6_1 import total_count
from lab_6.task_6_3 import create_list
from lab_6.task_6_9 import percent_count
from lab_6.task_6_4 import replace_word
from lab_6.task_6_6 import count_word


def test_total_count():
    actual = total_count()
    expected = f'Total of all numbers: 12149.0'
    assert actual == expected


def test_create_list():
    actual = create_list()
    expected = ['In Python you can doing general software development\n',
                'In Python you can diving into data science and math\n',
                'In Python you can speeding up and automating your workflow\n',
                'In Python you can building embedded systems and robots']
    assert actual == expected


def test_percent_count():
    actual = percent_count()
    expected = 'Upper letters in text= 2.09% \nLower letters in text= 97.91%'
    assert actual == expected


def test_replace_word():
    actual = replace_word()
    expected = 'In C you can doing general software development\n' \
               'In C you can diving into data science and math\n' \
               'In C you can speeding up and automating your workflow\n' \
               'In C you can building embedded systems and robots'
    assert actual == expected

