import re

import const_file


def chapters_list():
    with open(const_file.PATH + 'rob_crusoe.txt', 'r', encoding='utf-8') as r_crusoe,\
         open(const_file.PATH + 'chapters.txt', 'w', encoding='utf-8') as list_chapters:
        text = r_crusoe.read()
        pattern = r"CHAPTER [IVX]+—[A-Z ]+"
        chapters = re.findall(pattern, text)

        for chapter in chapters:
            list_chapters.write(f'chapter \n')


chapters_list()
