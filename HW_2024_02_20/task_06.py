# Task_06

ticket = input(': ')

n_1 = sum(int(i) for i in ticket[0:3])
n_2 = sum(int(i) for i in ticket[3:6])

if n_1 == n_2:
    print('yes')
else:
    print('no')
    
# Ввод_1:
#   183534 

# Вывод_1:
#   yes

# Ввод_2:
#   401367

# Вывод_2:
#   no


# комментарий преподавателя:
# я ожидал решения с математическими операциями, но тем не менее всё работает.