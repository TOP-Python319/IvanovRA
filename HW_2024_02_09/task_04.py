# Task_04

cell_1 = input()
cell_2 = input()

if (ord(cell_1[0]) - ord('a') + int(cell_1[1])) % 2 == 0:
    color_1 = 'white'
else:
    color_1 = 'black'
    
if (ord(cell_2[0]) - ord('a') + int(cell_2[1])) % 2 == 0:
    color_2 = 'white'
else:
    color_2 = 'black'

if color_1 == color_2:
    print('yes')
else:
    print('no')

# Ввод_1:
#   a1
#   b2

# Вывод_1:
#   yes

# Ввод_2:
#   f1
#   c3

# Вывод_2:
#   no

# комментарий преподавателя:
# всё чисто, вопросов нет. =)