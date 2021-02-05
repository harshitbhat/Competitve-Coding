T = int(input())
while T > 0:
    T = T - 1
    x,y = map(int,input().split())
    s = input()
    isPossible = False
    if x > 0 and y > 0:
        if s.count('R') >= x and s.count('U') >= y:
            isPossible = True
    elif x > 0 and y < 0:
        if s.count('R') >= x and s.count('D') >= abs(y):
            isPossible = True
    elif x < 0 and y > 0:
        if s.count('L') >= abs(x) and s.count('U') >= y:
            isPossible = True
    elif x < 0 and y < 0:
        if s.count('L') >= abs(x) and s.count('D') >= abs(y):
            isPossible = True
    elif x == 0:
        if y > 0:
            if s.count('U') >= y:
                isPossible = True
        elif y < 0:
            if s.count('D') >= abs(y):
                isPossible = True
    elif y == 0:
        if x > 0:
            if s.count('R') >= x:
                isPossible = True
        elif x < 0:
            if s.count('L') >= abs(x):
                isPossible = True
    if isPossible == True:
        print('YES')
    else:
        print('NO')