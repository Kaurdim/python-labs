def pif_table():
    print('Таблица Пифагора')
    for i in range(1, 11):
        print()
        for g in range(1, 11):
            res = i * g
            print(res, end=' ')
    print()

pif_table()