s = input()
ans = 1
z = s[0]
l = len(s)
for i in range(1,l):
    if s[i] == z:
        ans = ans + 1
    else:
        z = s[i]
        ans = 1
    if ans >= 7:
        break
if ans >=7:
    print('YES')
else:
    print('NO')