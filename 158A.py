n,k = map(int,input().split())
arr = list(map(int,input().split()))
t = arr[k-1]
ans = 0
for i in arr:
    if i >= t and i>0:
        ans = ans+1
print(ans)