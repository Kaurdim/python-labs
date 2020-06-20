def triangle_area():
    a = int(input('a='))
    b = int(input('b='))
    c = int(input('c='))

    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** (1/2)

    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('S=', S)
    return S

triangle_area()

