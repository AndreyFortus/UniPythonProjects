def number_check():
    number = int(input('Input integer value: '))
    with open('C:/Users/Andrii/Desktop/task_6_2.txt', 'w', encoding='utf-8') as file:
        file.write(f"number {number} is {'even' if number % 2 == 0 else 'odd'}")


number_check()
