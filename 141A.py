a = input()
b = input()
s = input()
check = {}
for i in s:
    if i not in check.keys():
        check[i] = 1
    else:
        check[i] += 1

isPossible = True
if len(s) != (len(a) + len(b)):
    isPossible = False
if isPossible == True:
    for i in a:
        if i not in check.keys() or check[i] == 0:
            isPossible = False
            break
        else:
            check[i] -= 1
    if isPossible == True:
        for i in b:
            if i not in check.keys() or check[i] == 0:
                isPossible = False
                break
            else:
                check[i] -= 1
if isPossible:
    print('YES')
else:
    print('NO')
