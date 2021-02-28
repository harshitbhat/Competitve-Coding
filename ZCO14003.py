n = int(input())
arr = []
for i in range(n):
    s = int(input())
    arr.append(s)
arr.sort()
ans = -1
for i in range(n):
    ans = max(ans,arr[i] * (n-i))
print(ans)