s = input()
orig = 'hello'
i = 0
j = 0
l = len(s)
while i<l:
    if s[i] == orig[j]:
        j = j+1
    i = i+1
    if(j==5):
        break
if j==5:
    print('YES')
else:
    print('NO')
