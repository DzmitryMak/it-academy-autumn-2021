"""List practice
1. Используйте генератор списков чтобы получить
 следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
"""


lst = [elem + elem2 for elem in 'ab' for elem2 in 'bcd']
print(lst)


"""
2. Используйте на предыдущий список slice чтобы получить
 следующий: ['ab', 'ad', 'bc']
"""
print(lst[::2])


"""
3. Используйте генератор списков чтобы
 получить следующий ['1a', '2a', '3a', '4a']
"""
lst_num = [elem + 'a' for elem in '1234']
print(lst_num)


"""
4. Одной строкой удалите элемент  '2a' из
прошлого списка и напечатайте его
"""
print(lst_num.pop(1))


"""
5. Скопируйте список из прошлого пункта и добавьте в него элемент '2a'
так чтобы в исходном списке этого элемента не было
"""
lst_last = lst_num.copy()

lst_last.insert(1, '2a')
print(lst_last, lst_num)