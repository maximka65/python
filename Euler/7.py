def is_prime(m):
    for i in range(2, m):
        if m % i == 0:
            return False
    return True


spisoc = []
n = 0

while n <= 10001:
    if is_prime(n):
        spisoc.append(n)
    n += 1
print(spisoc[-1])
