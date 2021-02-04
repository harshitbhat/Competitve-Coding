T =int(input())
while T > 0:
    T = T -1
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    myHash = {}
    for i in arr:
        if i in myHash.keys():
            myHash[i] += 1
        else:
            myHash[i] = 1
    a = list(myHash.keys())
    a.sort(reverse=True)
    i = 0
    ans = 0
    while i < k and i < len(a):
        ans += a[i]
        i += 1
    print(ans)
