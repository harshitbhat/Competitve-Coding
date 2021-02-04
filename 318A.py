n,k = map(int,input().split())
ans = 0
if n % 2 == 0:
    if k <= n // 2:
        ans = 2 * k - 1
    else:
        ans = 2 * (k - n//2)
else:
    if k <= n // 2 + 1:
        ans = 2 * k - 1
    else:
        ans = 2 * (k - n//2) - 2
print(ans)