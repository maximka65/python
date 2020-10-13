import timeit
import math
import cProfile

#n = int(input('введите длину массива: '))
n = 2000000
a = [True]*n


def func(n):
    global a
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if a[i] == True:
            j = i*i
            while j < n:
                a[j] = False
                j += i


func(n)

for i in range(2, len(a)):
    if a[i] == True:
        print(i)

# 100 loops, best of 5: 10.1 nsec per loop; for 20 numbers
# 100 loops, best of 5: 10 nsec per loop; for 500 numbers
# 1000 loops, best of 5: 9.07 nsec per loop; for 500 numbers

cProfile.run('func(n)')
# 6 function calls in 0.262 seconds; n = 1000000
# 6 function calls in 0.494 seconds; n = 2000000
