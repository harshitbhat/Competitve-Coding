T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    arr = list(map(int,input().split()))
    tempArr = []
    for i in range(n):
        tempArr.append([arr[i],i])
    tempArr.sort(key=lambda x : x[1])
    tempArr.sort(key=lambda x : x[0],reverse=True)
    k = 1
    ans = [0] * n
    for i in tempArr:
        ans[i[1]] = k
        k += 1
    ansStr = ''
    for i in ans:
        ansStr += str(i) + ' '
    print(ansStr)