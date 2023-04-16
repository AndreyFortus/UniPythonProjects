import io

with io.open('C:/Users/Andrii/Desktop/mon_cristo.txt', 'r', encoding='utf-8') as m_cristo:
    text = m_cristo.read()
    total_chars = len(text)
    num_upper = sum(1 for char in text if char.isalpha() and char.isupper())
    num_lower = sum(1 for char in text if char.isalpha() and char.islower())

    percent_upper = round(num_upper / total_chars * 100, 2)
    percent_lower = round(num_lower / total_chars * 100, 2)

    print(f'Upper letters in text = {percent_upper}% \nLower letters in text = {percent_lower}%')