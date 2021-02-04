s = input()
count1 = 0
count2 = 0
count3 = 0
l = len(s)
for i in range(0,l):
    if s[i] == '1':
        count1 = count1 + 1
    if s[i] == '2':
        count2 = count2 + 1
    if s[i] == '3':
        count3 = count3 + 1
ans = ''
while count1 > 0:
    ans = ans + '1+'
    count1 = count1 - 1
while count2 > 0:
    ans = ans + '2+'
    count2 = count2 - 1
while count3 > 0:
    ans = ans + '3+'
    count3 = count3 - 1

ans = ans[:-1]
print(ans)