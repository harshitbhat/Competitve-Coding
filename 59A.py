s = input()
upperCount = 0
lowerCount = 0
for i in s:
    if i.isupper() == True:
        upperCount = upperCount + 1
    else:
        lowerCount = lowerCount + 1

if upperCount > lowerCount:
    s = s.upper()
else:
    s = s.lower()

print(s)

