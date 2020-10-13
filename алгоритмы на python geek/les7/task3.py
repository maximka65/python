# 3. Массив размером 2m + 1, где m — натуральное число,
# заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

import random

size = int(input('введите нечетную длину массива: '))

a = [i for i in range(0, size)]
random.shuffle(a)
print(a)


def med(a):
    if len(a) % 2 == 0:
        raise ValueError
    else:
        for i in range(0, len(a)):
            sm = 0
            bg = -1
            for j in range(0, len(a)):
                if a[j] < a[i]:
                    sm += 1
                else:
                    bg += 1
            if sm == bg:
                return a[i]


print(med(a))
