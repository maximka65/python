import math
import cProfile


def prim_check(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def check(n):
    for i in range(2, n):
        if prim_check(i):
            print(i)


cProfile.run('check(1000000)')

# 3177 function calls in 0.003 seconds; n == 1000
# 9444 function calls in 0.009 seconds; n == 3000
# 31252 function calls in 0.039 seconds; n == 10000
# 3078664 function calls in 9.172 seconds; n == 1000000
