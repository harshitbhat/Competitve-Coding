T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    odd = 0
    for i in arr:
        if i % 2 != 0:
            odd += 1
    if odd % 2 == 0:
        print('1')
    else:
        print('2')
