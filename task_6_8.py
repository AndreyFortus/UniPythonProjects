import io
import re

with io.open('C:/Users/Andrii/Desktop/rob_crusoe.txt', 'r', encoding='utf-8') as r_crusoe,\
     io.open('C:/Users/Andrii/Desktop/chapters.txt', 'w', encoding='utf-8') as list_chapters:
    text = r_crusoe.read()
    chap_pattern = r"CHAPTER [IVX]+—[A-Z ]+"
    chapters = re.findall(chap_pattern, text)

    for chapter in chapters:
        list_chapters.write(chapter + '\n')
