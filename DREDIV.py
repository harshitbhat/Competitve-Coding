T = int(input())
while T > 0:
    T = T - 1
    n , k = map(int,input().split())
    arr = list(map(int,input().split()))
    arePossible = True
    if n == 1:
        if arr[0] % k != 0:
            arePossible = False
    else:
        arr.sort()
        maxMult = arr[len(arr)-1] + arr[len(arr)-2]
        multipleDict = {}
        i = 1
        while i*k <= maxMult:
            multipleDict[i*k] = True
            i += 1
        elementDict = {}
        for i in arr:
            elementDict[i] = True
        for i in arr:
            isPossibleForElement = False
            if i % k == 0:
                isPossibleForElement = True
            else:
                for z in multipleDict:
                    if (z - i) > 0:
                        if (z-i) in elementDict:
                            isPossibleForElement = True
                            break
            if isPossibleForElement == False:
                arePossible = False
                break
    if arePossible == True:
        print('YES')
    else:
        print('NO')
