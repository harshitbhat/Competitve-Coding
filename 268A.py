n = int(input())
arr  = []
for i in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)
ans = 0
for i in range(0,n):
    for j in range(0,n):
        if i != j:
            if arr[i][0] == arr[j][1]:
                ans += 1
print(ans)