# Task_04

user_number = int(input('Введите трёхзначное число: '))

if user_number >= 100 and 1000 > user_number:
    number_of_units = user_number % 10
    number_of_tens = int(user_number / 10) % 10
    number_of_hundreds = int(user_number / 100) % 10

    sum_of_numbers = number_of_hundreds + number_of_tens + number_of_units
    multiplication_of_number = number_of_hundreds * number_of_tens * number_of_units
    
    print(f"Сумма цифр = {sum_of_numbers}\n Произведение цифр = {multiplication_of_number}")
else:
    print('Введено некорректное число')

# Ввод:
#   Введите трёхзначное число: 123

# Вывод:
#   Сумма цифр = 6        
#   Произведение цифр = 6