"""
6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""

num = int(input('Введите число '))

n=num
rev_num = 0

while n > 0:
    rev_num = (rev_num*10)+n%10
    n = n//10
if rev_num == num:
    print('Число палиндром')
else:
    print('Не палиндром')