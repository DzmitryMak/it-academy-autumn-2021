"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента, равные
друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""
numbers = '1 1 3 4 5 3 1 4 6 3 2 5 6 2 4 3'
pairs = 0


numbers_lst = numbers.split()
arr = set(numbers_lst)

for num in arr:
    if numbers_lst.count(num) > 1:
        pair = (numbers_lst.count(num) * (numbers_lst.count(num) - 1)) / 2
        pairs += pair

print('Количество пар =', int(pairs))
