number = str(input('Введте число: '))
flow = int(input('Сколько последовательных цыфр? '))
vector = []


def maximum(m):
    m.sort()
    return m[-1]


for i in range(0, len(number)-flow-1):
    a = 1
    for j in range(0, flow):
        a *= int(number[i+j])
    vector.append(a)

print(maximum(vector))
