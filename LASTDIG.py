dig = [0,1,[6,2,4,8],[1,3,9,7],[6,4],5,6,[1,7,9,3],[6,8,4,2],[1,9]]
T = int(input())
while T > 0:
    T = T - 1
    a,b = map(int,input().split())
    a = a % 10
    ans = 0
    if b == 0:
        ans = 1
    else:
        if a == 0 or a == 1 or a == 5 or a == 6:
            ans = dig[a]
        elif a == 4 or a == 9:
            b = b % 2
            ans = dig[a][b]
        elif a == 2 or a == 3 or a == 7 or a == 8:
            b = b % 4
            ans = dig[a][b]
    print(ans)
    
