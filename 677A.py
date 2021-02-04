n,h = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
for i in arr:
    if i > h:
        ans = ans + 2
    else:
        ans = ans + 1
print(ans)