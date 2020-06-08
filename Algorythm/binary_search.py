import math

nr = int(input('Введите число елементов в списке: '))
spis = []

for i in range(0, nr):
    spis.append(int(input('Element nr {}: '.format(i))))

number = int(input('Введите искомый елемент: '))


def binary_search(n, l):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = math.ceil((low + high)/2)
        if n == spis[mid]:
            return mid
        elif n < spis[mid]:
            high = mid
        else:
            low = mid


print('Искомый елемент являится ', binary_search(number, spis), ' в списке.')
