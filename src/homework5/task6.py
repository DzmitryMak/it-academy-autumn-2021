"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def div(num):
    i = 0
    if num % 2:
        return print('число не делится на 2')

    while not num % 2:
        num = num >> 1
        i += 1

    return print('максимальны делитель, являющийся степенью двойки =', 2**i)


div(24)
# div(78)
# div(240)