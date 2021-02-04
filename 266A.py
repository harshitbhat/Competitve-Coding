n = int(input())
s = input()
ans = 0
diff = s[0]
for i in range(1,n):
    if s[i] == diff:
        ans = ans + 1
    else:
        diff = s[i]
print(ans)
