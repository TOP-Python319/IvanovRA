# Task_03

HOUR = 60

enter_minutes = int(input('Введите минуты: '))
user_hours = enter_minutes // HOUR
user_minutes = enter_minutes % HOUR

print(f"{enter_minutes} мин - это {user_hours} час {user_minutes} мин")

# Вывод:
#     Введите минуты: 650
#     650 мин - это 10 час 50 мин