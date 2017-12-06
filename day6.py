inp = '''2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14'''


def first():
    num = list(map(int, inp.split()))
    states = {}
    c = 0
    while ''.join(map(str, num)) not in states:
        states[''.join(map(str, num))] = c
        i = get_max()
        v = num[i]
        num[i] = 0
        while v:
            i += 1
            num[i % len(num)] += 1
            v -= 1
        c += 1

    print(c, c - states[''.join(map(str, num))])


def get_max():
    m_i = 0
    m = -1
    for i in range(len(inp)):
        if inp[i] > m:
            m_i = i
            m = inp[i]
    return m_i


first()
