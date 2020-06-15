d = 0


class Buffer:
    def __init__(self):
        self.list = []

    def add(self, *a):
        if len(a) < 5:
            self.list = a
        else:
            for i in list(range(int(len(a)/5))):
                global d
                print(a[0+d]+a[1+d]+a[2+d]+a[3+d]+a[4+d])
                m = a[d:4+d]
                d += 5
            self.list = list(set(a) - set(m))

    def get_current_part(self):
        print(self.list)


buf = Buffer()
buf.add(1, 3, 4, 3, 4, 62, 7, 4, 6, 8, 2, 3)
buf.get_current_part()


#new line