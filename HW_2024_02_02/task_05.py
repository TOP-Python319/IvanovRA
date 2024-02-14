# Task_05

whole_miles = input("Введите целое количество миль: ")
fractional_miles = input("Введите дробное количество миль: ")

miles = float("{0}.{1}".format(whole_miles, fractional_miles))
kilometers = miles * 1.61

print(f"{miles: .1f} миль ={kilometers: .1f} км")

# Ввод:
#     Введите целое количество миль: 35
#     Введите дробное количество миль: 5

# Вывод:
#     35.5 миль = 57.2 км