# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например,
#  если введено число 34560,
#  в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import sys

n = int(input('введите число: '))
a = []

for i in range(0, len(str(n))):
    a.append(n - (n // 10) * 10)
    n = n // 10

a1, a2 = 0, 0

for i in range(0, len(a)):
    if i % 2 == 0:
        a1 += 1
    else:
        a2 += 1
print('четных чисел: ', a1)
print('нечетных чисел: ', a2)

# print(sys.version, sys.platform)
# macOS 10.14.5  x64
# python 3.7.4
# код без оптимизации
# print(sys.getsizeof(n), sys.getsizeof(a), sys.getsizeof(a1), sys.getsizeof(a2))
# память на переменые затрачено 24 + 136 + 28 + 28 = 216
