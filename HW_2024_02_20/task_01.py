# Task_01

list_of_num = []

while True:
    num = int(input(': '))
    if num % 7 == 0:
        list_of_num.append(num)
    else:
        print(' '.join(map(str, reversed(list_of_num))))
        break

# Ввод:
#   : 7
#   : 14
#   : 21
#   : 28
#   : 35
#   : 42
#   : 44

# Вывод:
#   42 35 28 21 14 7

# комментарий преподавателя:
# всё чисто, вопросов нет. =)
