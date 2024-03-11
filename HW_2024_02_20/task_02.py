# Task_02

sum_of_num = 0
quantity = int(input('amount of numbers: '))
count = 1

while count <= quantity:
    num = int(input('enter number: '))
    if num > 0:
        sum_of_num += num
    count += 1

print(sum_of_num)
    
# Ввод_1:
#   amount of numbers: 7
#   enter number: 5
#   enter number: 0
#   enter number: -10
#   enter number: 7
#   enter number: -1
#   enter number: 23
#   enter number: 0

# Вывод_1:
#   35

