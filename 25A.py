n = int(input())
arr = list(map(int,input().split()))
odd = 0
even = 0
for i in arr:
    if i%2==0:
        even = even + 1
    else:
        odd = odd + 1

ans = 0
if even == 1:
    for i in range(0,n):
        if arr[i] % 2 == 0:
            ans = i
            break
else:
    for i in range(0,n):
        if arr[i] % 2 != 0:
            ans = i
            break
print(ans+1)