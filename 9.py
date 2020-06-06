def mm(a, b, c):
    if a < b < c:
        return True
    else:
        return False


def pit(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


def sotca(a, b, c):
    if a+b+c == 1000:
        return True
    else:
        return False


for i in range(1, 500):
    for j in range(1, 500):
        for l in range(1, 500):
            if mm(l, j, i) and pit(l, j, i) and sotca(l, j, i):
                print(l, j, i)
