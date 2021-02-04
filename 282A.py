t = int(input())
ans = 0
while t>0:
    t = t-1
    s = input()
    for i in s:
        if i == '+':
            ans = ans + 1
            break
        if i == '-':
            ans = ans - 1
            break
print(ans)