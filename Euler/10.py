def is_prime(m):
    if m < 2:
        return False
    for i in range(2, m):
        if m % i == 0:
            return False
    return True


n = 0
suma = 0

while n <= 2000000:
    if is_prime(n):
        print(n)
        suma += n
    n += 1

print(suma)
