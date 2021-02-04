s = input()
while s[0:3] == 'WUB':
    s = s[3:]
while s[-3:] == 'WUB':
    s = s[:-3]
s = s.replace('WUB',' ')
print(s)