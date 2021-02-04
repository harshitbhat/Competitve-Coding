T = int(input())
while T > 0:
    T = T - 1
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    s = 0
    for i in arr:
        s = s + i
    if s % k == 0:
        print(0)
    else:
        print(1)

