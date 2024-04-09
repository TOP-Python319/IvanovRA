# Task_08

num1 = num2 = 1
 
n = int(input(": "))
 
print(num1, num2, end=' ')
 
for i in range(2, n):
    num1, num2 = num2, num1 + num2
    print(num2, end=' ')
    
# Ввод_1:
#   17
#   

# Вывод_1:
#   1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 


# комментарий преподавателя:
