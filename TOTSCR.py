T = int(input())
while T > 0:
    T -= 1
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    otp = []
    for i in range(n):
        ans = 0
        s = input()
        for j in range(k):
            if s[j] == '1':
                ans += a[j]
        otp.append(ans)
    for i in otp:
        print(i)