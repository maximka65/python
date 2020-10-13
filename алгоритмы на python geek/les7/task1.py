# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random

a = [i for i in range(-100, 100)]
random.shuffle(a)
print(a)


def sort(a):
    n = 0
    while n < len(a):
        for i in range(0, len(a)-1):
            if a[i+1] < a[i]:
                a[i+1], a[i] = a[i], a[i+1]
        n += 1
    return a


print(sort(a))
