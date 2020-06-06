def fib(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


s = 0
y = 0
while True:

    y += 1
    if fib(y) % 2 == 0:
        s += fib(y)
    if s >= 4000000:
        s -= fib(y)
        break

print(s)
