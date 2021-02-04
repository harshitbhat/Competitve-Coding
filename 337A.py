n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = 999999
for i in range(0,m):
    if(i+n-1) < m:
        ans = min(ans,arr[i+n-1]-arr[i])
    else:
        break
print(ans)

