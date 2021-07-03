hight = int(input())


for i in range(hight):
    for j in reversed(range(hight)):
        if i < j:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(hight):
        if i > j:
            print('*', end='')
    print()
