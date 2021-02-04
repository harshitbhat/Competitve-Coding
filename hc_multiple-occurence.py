T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    store = {}
    for i in range(0,n):
        store[arr[i]] = []
    for i in range(0,n):
        store[arr[i]].append(i+1)
    ans = 0
    for i in store:
        ans = ans + store[i][len(store[i]) - 1] - store[i][0]
    print(ans)
