def hasDistinct(num):
    hasDup = {}
    for i in num:
        hasDup[i] = 1
    if len(hasDup) == 4:
        return True
    else:
        return False

s = int(input())
s = s + 1
found = False
while found == False:
    if hasDistinct(str(s)):
        found = True
    else:
        s = s + 1
print(s)
