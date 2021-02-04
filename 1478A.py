T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    store = {}
    for i in arr:
        if i in store.keys():
            store[i] += 1
        else:
            store[i] = 1
    ans = 0
    for i in store:
        ans = max(ans,store[i])
    print(ans)