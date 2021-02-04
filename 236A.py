s = input()
l = len(s)
myhash = {}
for i in range(0,l):
    myhash[s[i]] = 1

if len(myhash) %2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')