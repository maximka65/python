"""  4. Пользователь вводит две буквы. Определить, 
на каких местах алфавита они стоят, и сколько между ними находится букв. """

import math

a = input('введите первую букву ')
b = input('введите вторую букву ')

print('первая буква находится на позиции ', ord(a) - ord('a') + 1)
print('вторая буква находится на позиции ', ord(b) - ord('a') + 1)


print('растояние между ними ', math.fabs(ord(b) - ord(a)) + 1, ' букв')
