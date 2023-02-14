print('Zadacha_1')
'''Напишите программу, которая на вход принимает два числа A и B, и 
возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''

def exponentiation(b: int):
    for i in range(b+1):
        if b == 1:
            return a
    return a*(exponentiation(b - 1))
a = int(input('->'))
b = int(input('->'))
print(exponentiation(b))

print('Zadacha_2 ')
'''Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
неотрицательных чисел. Из всех арифметических операций допускаются 
только +1 и -1. Также нельзя использовать циклы.
2 2
4'''

def sum_numbers(a, b: int):
        if a == 0:
            return b
        elif a < 0:
            return sum_numbers(a + 1, b - 1)
        return sum_numbers(a - 1, b + 1)
first_number = int(input('->'))
second_number = int(input('->'))
print(sum_numbers(first_number, second_number))