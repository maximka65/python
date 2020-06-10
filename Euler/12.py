import math

triangle_numbers_list = []
# prim numbers


def is_sq(n):
    if math.ceil(n**(1/2)) == n**(1/2):
        return True
    else:
        return False

# function returns Nth triangle number


def triangle(n):
    m = 0
    counter = 1
    tri_number = 1
    while m < n-1:
        counter += 1
        tri_number += counter
        m += 1
    return tri_number

# function returns how much dividers number has


def deviders(n):
    s = 1
    for i in range(1, math.ceil(n**(1/2))):
        if n % i == 0:
            s += 2
            if is_sq(n):
                s -= 1
    return s


m = 1000
n = triangle(m)
while deviders(n) < 500:
    m += 1
    n = triangle(m)

print(n)
