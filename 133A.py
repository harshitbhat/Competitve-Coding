s = input()
has = False
for i in s:
    if i == 'H' or i == 'Q' or i == '9':
        has = True
if has == True:
    print('YES')
else:
    print('NO')