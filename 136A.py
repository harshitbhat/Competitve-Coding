n = int(input())
arr = list(map(int,input().split()))
indexHash = {}
for i in range(0,n):
    indexHash[arr[i]] = i+1
for i in range(0,n):
    print(indexHash[i+1],end=" ")
print()
