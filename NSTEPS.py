T = int(input())
while T > 0:
    T = T - 1
    x, y = map(int,input().split())
    if x == y:
        n = int(x/2) + 1
        if x % 2 == 0:
            print(4*n - 4)
        else:
            print(4*n - 3)
    elif (x - y) == 2:
        n = int(x/2)
        if x % 2 == 0:
            print(4*n - 2)
        else:
            print(4*n - 1)
    else:
        print('No Number')