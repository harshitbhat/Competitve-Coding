n = int(input())
arr = list(map(int,input().split()))
minInd = n - 1 - arr[::-1].index(min(arr))
maxInd = arr.index(max(arr))
ans = -1
if maxInd > minInd:
    ans = maxInd + n - minInd - 2
else:
    ans = maxInd + n - 1 - minInd
print(ans)