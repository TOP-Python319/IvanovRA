# Task_06

cell_1 = input()
cell_2 = input()

if abs(ord(cell_1[0]) - ord(cell_2[0])) <= 1 and abs(int(cell_1[1]) - int(cell_2[1])) <= 1:
    print('yes')
else:
    print('no')
    
# Ввод_1:
#   g3
#   f2

# Вывод_1:
#   yes

# Ввод_2:
#   c6
#   d4

# Вывод_2:
#   no