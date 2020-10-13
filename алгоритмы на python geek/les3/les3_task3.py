# 3. В массиве случайных целых чисел поменять
# местами минимальный и максимальный элементы.

import random

a = []

for i in range(0, 20):
    a.append(random.randrange(1, 100, 1))

print(a)
mx1 = max(a)
mn1 = min(a)

for i in range(0, 20):
    if a[i] == mx1:
        mx = i
    elif a[i] == mn1:
        mn = i

a[mx] = mn1
a[mn] = mx1

print(a)
