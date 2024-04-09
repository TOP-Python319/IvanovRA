# Task_04

number = int(input(": "))
end_number = int('1' + '0' * number)
start_number = end_number // 10
count = 0
for num in range(start_number, end_number):
    for i in range(2, num):
        if num % i == 0:
            break
        elif num % i != 0 and i == num - 1:
            count += 1
            
print(count)  

# Ввод_1:
#  3
#   

# Вывод_1:
#  143


# комментарий преподавателя:
# всё верно, однако можно сделать оптимизацию в цикле ограничив правую границу в range