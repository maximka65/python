import time

n = 20
m = True
cart1 = []
for i in range(3, 20):
    cart1.append(1)
while m:
    n += 20
    cart2 = []
    for i in range(3, 20):
        if n % i != 0:
            cart2.append(0)
        else:
            cart2.append(1)
    if cart2 == cart1:
        m = False
    del cart2
print('final ', n)
