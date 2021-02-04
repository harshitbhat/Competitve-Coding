T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    s = input()
    countO = 0
    for i in s:
        if i == '0':
            countO = countO + 1
    if countO > 30:
        print('NO')
    else:
        print('YES')