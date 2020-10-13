# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего
# и ниже среднего
from collections import namedtuple

n = int(input('введите количество предприятий: '))
a = []
company = namedtuple(
    'companies', 'name, profit1, profit2, profit3, profit4, med', defaults=[0])


for i in range(0, n):
    print(i+1)
    x = input('название: ')
    y1 = int(input('прибыль 1 кв: '))
    y2 = int(input('прибыль 2 кв: '))
    y3 = int(input('прибыль 3 кв: '))
    y4 = int(input('прибыль 4 кв: '))
    a.append(company(x, y1, y2, y3, y4))

# print(a)
medmed = 0

for i in range(0, n):
    med = (a[i].profit1 + a[i].profit2 + a[i].profit3 + a[i].profit4) / 4
    a[i] = a[i]._replace(med=med)
    medmed += med

medmed = medmed/n
sm = []
bg = []

for i in range(0, n):
    if a[i].med <= medmed:
        sm.append(a[i])
    else:
        bg.append(a[i])

print('средняя прибыль: ', medmed)
print(sm, bg)

print('прибыль меньше среднего у компаний: ')
for i in range(0, len(sm)):
    print(sm[i].name, ': ', sm[i].med)

print('прибыль больше среднего у компаний: ')
for i in range(0, len(sm)):
    print(bg[i].name, ': ', bg[i].med)
