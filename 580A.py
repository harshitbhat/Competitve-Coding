n = int(input())
arr = list(map(int,input().split()))
length = [0] * n 
length[0] = 1
ans = 1
if n > 1:
    for i in range(0,n):
        if arr[i-1] <= arr[i]:
            length[i] = length[i-1] + 1
        else:
            length[i] = 1
    ans = 1
    for i in length:
        if i > ans:
            ans = i
print(ans)
