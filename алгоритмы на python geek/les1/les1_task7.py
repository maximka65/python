""" 7. Определить, является ли год, который ввел пользователь, 
високосным или не високосным. """

a = int(input('введите год '))

if a % 4 == 0:
    print('год весокосный')
else:
    print('год невесокосный')
