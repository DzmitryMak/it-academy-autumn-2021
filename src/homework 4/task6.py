"""
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним
или большим числом пробелов или символами конца строки (\n).
Определите, сколько различных слов содержится в этом тексте.
"""

text = input('Введите текст ')

lst = set(text.split())

print('Различных слов -', len(lst))
