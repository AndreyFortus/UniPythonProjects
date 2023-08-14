import re

import lab_6.constants


def chapters_list():
    with open(lab_6.constants.PATH + 'rob_crusoe.txt', 'r', encoding='utf-8') as r_crusoe,\
         open(lab_6.constants.PATH + 'chapters.txt', 'w', encoding='utf-8') as list_chapters:
        text = r_crusoe.read()
        pattern = r"CHAPTER [IVX]+—[A-Z ]+"
        chapters = re.findall(pattern, text)

        for _ in chapters:
            list_chapters.write(f'chapter \n')


if __name__ == '__main__':
    chapters_list()
