import re

from constants import PATH


def separate_text():
    with open(PATH + 'text_example.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    pattern = r'(?<=[.!?])\s+'
    return re.split(pattern, text)


if __name__ == '__main__':
    i = 1
    for sentence in separate_text():
        print(f'Sentence {i}: {sentence}')
        i += 1
