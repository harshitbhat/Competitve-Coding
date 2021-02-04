n = int(input())
ans = 1
s = input()
last = s[1]
n = n-1
while n > 0:
    s = input()
    n = n-1
    if last == s[0]:
        last = s[1]
        ans = ans + 1

print(ans)
