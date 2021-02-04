T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    bS = input()
    b = list(map(int,bS))
    a = [0] * n
    s = [0] * n
    a[0] = 1
    s[0] = a[0] + b[0]
    for i in range(1,n):
        if b[i] == 0:
            if s[i-1] == 0 or s[i-1] == 2:
                a[i] = 1
            else:
                a[i] = 0
        else:
            if s[i-1] == 2:
                a[i] = 0
            else:
                a[i] = 1
        s[i] = b[i] + a[i]
    for i in a:
        print(i,end="")
    print()
