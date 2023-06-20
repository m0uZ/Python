# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import math


# функция для нахождения суммы и произведения дробей
def add_mult_fractions(frac1, frac2):
    num1, den1 = map(int, frac1.split('/'))
    num2, den2 = map(int, frac2.split('/'))
    
    # находим общий знаменатель
    lcm = (den1 * den2) // math.gcd(den1, den2)
    
    # находим сумму числителя и знаменателя
    sum_num = lcm // den1 * num1 + lcm // den2 * num2
    sum_den = lcm
    
    # произведения числителя и знаменателя
    mult_num = num1 * num2
    mult_den = den1 * den2
    
    # находим наибольший общий делитель произведения числителя и знаменателя
    g = math.gcd(mult_num, mult_den)
    
    # сокращаем произведение, если это возможно
    mult_num //= g
    mult_den //= g
    
    # возвращаем сумму и произведение в виде строковых дробей
    return f"{sum_num}/{sum_den}", f"{mult_num}/{mult_den}"


frac1 = input('Введите первую дробь: ')
frac2 = input('Введите вторую дробь: ')

sum_frac, mult_frac = add_mult_fractions(frac1, frac2)
print(f"Сумма дробей: {sum_frac}")
print(f"Произведение дробей: {mult_frac}")

