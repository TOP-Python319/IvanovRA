w# Task_03

n = int(input("Введите натуральное число: "))
sum_of_divisors = 0
for i in range(1, n + 1):
    if n % i == 0:
        sum_of_divisors += i
print(f'Сумма делителей числа {n} = {sum_of_divisors}')
    
# Ввод_1:
#   Введите натуральное число: 50


# Вывод_2:
#   Сумма делителей числа 50 = 93


# комментарий преподавателя:
# всё верно
