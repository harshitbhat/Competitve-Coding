T = int(input())
while T > 0:
    T = T - 1
    s = input()
    ans = 0
    if s[0] == '1':
        ans = 1
    for i in range(1,len(s)):
        if s[i] == '1' and s[i-1] == '0':
            ans += 1
    print(ans)