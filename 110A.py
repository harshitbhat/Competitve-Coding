lucky = [4,7,44,47]
s = input()
count = 0
for i in s:
    if i == '4' or i =='7':
        count = count + 1 
isLucky = False
for i in lucky:
    if count == i:
        isLucky = True
if isLucky == True:
    print('YES')
else:
    print('NO')