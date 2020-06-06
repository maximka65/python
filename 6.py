m = 100


def sum_sqr(n):
    suma = 0
    for i in range(1, n+1):
        suma += i**2
    return suma


def sqr_sum(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma**2


print('Diferenta dintre patratul sumei ', sqr_sum(m) - sum_sqr(m))
