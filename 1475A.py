T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    while n % 2 == 0:
        n = n / 2
    if n == 1:
        print('NO')
    else:
        print('YES')