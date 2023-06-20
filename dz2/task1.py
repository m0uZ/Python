# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))

print(hex(num))

hex_digits = '0123456789ABCDEF'
result = ''

if num == 0:
    result = '0'
else:
    while num > 0:
        digit = num % 16
        result = hex_digits[digit] + result
        num //= 16

print(f'Шестнадцатеричное представление числа: {result}')
