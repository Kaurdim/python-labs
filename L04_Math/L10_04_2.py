def fib(n):
    a = 0
    b = 1

    print('1 ->', b)

    for i in range(2, n + 1):
        a, b = b, b + a
        print('{0} -> {1}'.format(i, b))


n = int(input('n='))
fib(n)
