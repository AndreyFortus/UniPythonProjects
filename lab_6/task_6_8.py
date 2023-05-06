import io
import re


def chapters_list():
    with io.open('C:/Users/Andrii/Desktop/rob_crusoe.txt', 'r', encoding='utf-8') as r_crusoe,\
         io.open('C:/Users/Andrii/Desktop/chapters.txt', 'w', encoding='utf-8') as list_chapters:
        text = r_crusoe.read()
        pattern = r"CHAPTER [IVX]+—[A-Z ]+"
        chapters = re.findall(pattern, text)

        for chapter in chapters:
            list_chapters.write(chapter + '\n')


chapters_list()
