def all_sum():
    sum = 0
    a = 0
    while True:
        a = int(input('a='))
        if a == 0:
            break
        sum += a

    print('Сумма =', sum)

def all_sum2():
    sum = 0
    a = 1
    while (a != 0):
        a = int(input('a='))
        sum += a

    print('Сумма =', sum)

# all_sum()
all_sum2()

