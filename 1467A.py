T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    a = [0] * n
    if n == 1:
        a[0] = 9
    elif n == 2:
        a[0] = 9
        a[1] = 8
    elif n == 3:
        a[0] = 9
        a[1] = 8
        a[2] = 9
    else:
        a[0] = 9
        a[1] = 8
        a[2] = 9
        k = 0
        for i in range(3,n):
            a[i] = k
            k += 1
            if(k == 10):
                k = 0
    for i in a:
        print(i,end='')
    print()