import sys
T = int(input())
while T > 0:
    T = T - 1
    n , k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    inf = -sys.maxsize
    if n  == 1:
        ans = -1
    else:
        h1 = arr[0]
        arr[0] = inf
        ans = 1
        i = 1
        while i < n and h1 < k:
            if arr[i] == inf:
                i += 1
                continue
            else:
                foundLower = False
                j = n-1
                while j > i:
                    if (k - h1) < arr[j]:
                        foundLower = True
                        h1 += arr[j]
                        arr[j] = inf
                        ans += 1
                        break
                    j -= 1
                if foundLower == False:
                    h1 += arr[i]
                    arr[i] = inf
                    i += 1
                    ans += 1
        if h1 >= k:
            forH2 = []
            for i in arr:
                if i != inf:
                    forH2.append(i)
            if len(forH2) == 0:
                ans = -1
            else:
                forH2.sort(reverse=True)
                preSum = []
                preSum.append(forH2[0])
                for i in range(1,len(forH2)):
                    preSum.append(preSum[i-1] + forH2[i])
                i = 0
                h2 = 0
                while i < n:
                    h2 = preSum[i]
                    ans += 1
                    if h2 >= k:
                        break
                    i += 1
        else:
            ans = -1
    if h1 < k or h2 < k:
        ans = -1
    print(ans)