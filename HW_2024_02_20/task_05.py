# Task_05

message = input(': ')
msg = message.split()
msg = ''.join(msg)
x = len(msg)
y = x * 30
price_in_rub = y // 100
price_in_cop = y % 100
print(f'{price_in_rub} руб. {price_in_cop} коп.')
    
# Ввод_1:
#   грузите апельсины бочках братья карамазовы

# Вывод_1:
#   11 руб. 40 коп.

