T = int(input())
while T > 0:
    T = T - 1
    n,m = map(int,input().split())
    z = n // 2
    if m <= z:
        print('Yes')
    else:
        print('No')