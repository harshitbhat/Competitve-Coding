T = int(input())
while T > 0:
    T -= 1
    s = input()
    l = len(s)
    isLapinDrome = True
    if l % 2 == 0:
        a = list(s[0:l//2])
        b = list(s[l//2:l])
        a.sort()
        b.sort()
        if a != b:
            isLapinDrome = False
    else:
        a = list(s[0:l//2])
        b = list(s[l//2 + 1:l])
        a.sort()
        b.sort()
        if a != b:
            isLapinDrome = False
    if isLapinDrome:
        print('YES')
    else:
        print('NO')