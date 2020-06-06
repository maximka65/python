import math

x = 600851475143


def is_simple(a):
    for i in range(2, math.ceil(a**(1/2))+1):
        if a % i == 0:
            return False
    return True


for i in reversed(range(1, math.ceil(x**(1/2))+1)):
    if x % i == 0 and is_simple(i):
        break
print(i)
