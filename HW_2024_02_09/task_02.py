# Task_02

n1 = int(input())
n2 = int(input())

if n1 % n2 == 0:
    print(f'{n1} делится на {n2} нацело')
    print(f'частное: {n1 // n2}')
else:
    print(f'{n1} не делится на {n2} нацело')
    print(f'неполное частное: {n1 // n2} ')
    print(f'остаток: {n1 % n2}')
    
# Ввод_1:
#   16
#   4

# Вывод_1:
#   16 делится на 4 нацело
#   частное: 4

# Ввод_2:
#   20
#   6

# Вывод_2:
#   20 не делится на 6 нацело
#   неполное частное: 3 
#   остаток: 2

# комментарий преподавателя:
# всё чисто, вопросов нет. =)