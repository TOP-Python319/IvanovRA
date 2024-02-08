# Task_01

first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
year_of_birth = int(input('Введите год рождения: '))

THIS_YEAR = 2024
user_age = THIS_YEAR - year_of_birth

print(last_name, ' ', first_name,', ', user_age, sep='')

# Вывод:
#     Введите имя: Oleg
#     Введите фамилию: Ivanov
#     Введите год рождения: 1999
#     Ivanov Oleg, 25