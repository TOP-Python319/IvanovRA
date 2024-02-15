# Task_03

year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('yes')
else:
    print('no')
    
# Ввод_1:
#   2024

# Вывод_1:
#   yes

# Ввод_2:
#   1900

# Вывод_2:
#   no

