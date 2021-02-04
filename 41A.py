s = input()
t = input()
l1 = len(s)
l2 = len(t)
isSame = True
if l1 == l2:
    for i in range(0,l1):
        if s[i] != t[l1-i-1]:
            isSame = False
else:
    isSame = False
if isSame == True:
    print('YES')
else:
    print('NO')