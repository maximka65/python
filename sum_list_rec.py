def sum(l):
    if l == []:
        return 0
    else:
        i = l[-1]
        del l[-1]
        return i + sum(l)


list1 = [1, 5, 8, 4, 2]

print(sum(list1))
