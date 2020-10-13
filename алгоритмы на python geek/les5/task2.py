# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого — цифры числа.
from collections import namedtuple

a = namedtuple('numbers', 'hex dec')
b = namedtuple('numbers', 'hex dec')
print('вводите числа большими буквами как в примере!')
a.dec, b.dec = list(input('введите первое число: ')), list(
    input('введите второе число: '))

a.dec = a.dec[::-1]
b.dec = b.dec[::-1]

a10 = 0
b10 = 0

n = 0
for i in a.dec:
    try:
        a10 += int(i) * (16 ** n)
        n += 1
    except ValueError:
        a10 += int(ord(i) - 55) * (16 ** n)
        n += 1

n = 0
for i in b.dec:
    try:
        b10 += int(i) * (16 ** n)
        n += 1
    except ValueError:
        b10 += int(ord(i) - 55) * (16 ** n)
        n += 1

sum10 = a10 + b10
pr10 = a10 * b10
sum16 = []
pr16 = []

for i in range(1, len(str(sum10))):
    sum16.append(sum10 % 16)
    sum10 = sum10 // 16

for i in range(1, len(str(pr10))):
    pr16.append(pr10 % 16)
    pr10 = pr10 // 16

sum16 = sum16[::-1]
pr16 = pr16[::-1]
s = ''
p = ''

for i in sum16:
    if i < 10:
        s += str(i)
    if i == 10:
        s += 'A'
    if i == 11:
        s += 'B'
    if i == 12:
        s += 'C'
    if i == 13:
        s += 'D'
    if i == 14:
        s += 'E'
    if i == 15:
        s += 'F'

for i in pr16:
    if i < 10:
        p += str(i)
    if i == 10:
        p += 'A'
    if i == 11:
        p += 'B'
    if i == 12:
        p += 'C'
    if i == 13:
        p += 'D'
    if i == 14:
        p += 'E'
    if i == 15:
        p += 'F'

print('сумма:', s)
print('произведение:', p)
