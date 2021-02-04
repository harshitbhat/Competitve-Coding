t = int(input())
ans = 0
while t > 0:
    t = t-1
    p , q = map(int,input().split())
    if (q - p) >=2:
        ans = ans + 1
print(ans)