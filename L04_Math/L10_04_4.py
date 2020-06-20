def numbers_difference():
    a = int(input('a = '))
    b = int(input('b = '))
    diff = 0
    if a > b:
        diff = a - b
    else:
        diff = b - a
    print('Разность =', diff)


numbers_difference()
