T = int(input())
while T > 0:
    T = T - 1
    x,y,k,n = map(int,input().split())
    i = x
    j = y
    if i > j:
        i = y
        j = x
    if (j-i)%(2*k) == 0:
        print('Yes')
    else:
        print('No')