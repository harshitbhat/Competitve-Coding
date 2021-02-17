n = int(input())
arr = [100,20,10,5,1]
ans = 0
for i in arr:
    ans += n // i
    n = n % i
print(ans)