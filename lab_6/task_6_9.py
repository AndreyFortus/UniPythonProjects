def percent_count():
    with open('C:/Users/Andrii/Desktop/mon_cristo.txt', 'r', encoding='utf-8') as m_cristo:
        text = m_cristo.read()
        total_chars = len(text)
        num_upper = sum(1 for char in text if char.isalpha() and char.isupper())

        percent_upper = round(num_upper / total_chars * 100, 2)
        percent_lower = 100 - percent_upper

        print(f'Upper letters in text= {percent_upper}% \nLower letters in text= {percent_lower}%')


percent_count()
