n = int(input())
arr = list(map(int,input().split()))
arr.sort()
cummulative = []
cummulative.append(arr[0])
for i in range(1,n):
    cummulative.append(arr[i] + cummulative[i-1])
backSum = arr[n-1]
i = n-1
while i > 0:
    if backSum > cummulative[i-1]:
        break
    else:
        backSum = backSum + arr[i-1]
        i = i-1
print(n-i)