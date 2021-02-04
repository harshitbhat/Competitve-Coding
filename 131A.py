s = input()
areAllCaps = True
for i in s:
    if i.islower():
        areAllCaps = False
        break
isFirstLowerAndRestCaps = True
if s[0].islower() == False:
    isFirstLowerAndRestCaps = False
else:
    for i in range(1,len(s)):
        if s[i].islower() == True:
            isFirstLowerAndRestCaps = False

if areAllCaps == True or isFirstLowerAndRestCaps == True:
    for i in s:
        if i.islower():
            print(i.upper(),end='')
        if i.isupper():
            print(i.lower(),end='')
    print()
else:
    print(s)