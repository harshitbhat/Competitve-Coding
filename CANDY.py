while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    sumCan = 0
    for i in range(n):
        z = int(input())
        arr.append(z)
        sumCan = sumCan + z
    if sumCan % n == 0:
        ans = 0
        each = int(sumCan / n)
        for i in arr:
            if i < each:
                ans += each - i
        print(ans)
    else:
        print(-1)