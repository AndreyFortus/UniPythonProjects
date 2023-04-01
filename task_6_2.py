number = int(input('Input integer value: '))
with open('C:/Users/Andrii/Desktop/task_6_2.txt', 'w') as t2:
    if number % 2 == 0:
        t2.write(f'number {number} is even')
    else:
        t2.write(f'number {number} is odd')
