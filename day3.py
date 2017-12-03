INP = 312051
D = [(1, 0),
     (1, 1),
     (0, 1),
     (-1, 1),
     (-1, 0),
     (-1, -1),
     (0, -1),
     (1, -1)]


def get_spiral_point():
    x = 0
    y = 0
    s = 1
    while 1:
        for i in [1, -1]:
            for d in range(1, s + 1):
                yield x + d * i, y
            x += s * i
            for d in range(1, s + 1):
                yield x, y + d * i
            y += s * i
            s += 1


def first():
    it = iter(get_spiral_point())
    for i in range(INP - 2):
        next(it)
    print(sum(map(abs, next(it))))


def second():
    a = [[0 for _ in range(200)] for _ in range(200)]
    a[100][100] = 1
    for c in get_spiral_point():
        c = c[0] + 100, c[1] + 100
        a[c[1]][c[0]] = sum(a[c[1] + i[1]][c[0] + i[0]] for i in D)
        if a[c[1]][c[0]] > 312051:
            print(a[c[1]][c[0]])
            break


first()
second()
