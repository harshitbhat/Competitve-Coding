t = int(input())
while t > 0:
    t = t - 1
    n = int(input())
    ans = 0
    i = 1
    while True:
        z = int(n/(5**i))
        if z == 0:
            break
        ans += int(n/(5**i))
        i = i + 1
    print(ans)