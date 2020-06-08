def poli(x):
    mi = str(x)
    y = int(len(mi)/2)
    if not len(mi) % 2 == 0:
        return False
    elif mi[y:] == ''.join(reversed(mi[0:y])):
        return True
    else:
        return False


m = []
n = []


for i in list(reversed(range(100, 1000))):
    for j in list(reversed(range(100, 1000))):
        if poli(i*j):
            m.append(i)
            n.append(j)

print(m[0], ' * ', n[0])
