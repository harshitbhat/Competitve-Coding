a = input()
b = input()
a = a.lower()
b = b.lower()

l = len(a)
ans = 0

for i in range(0,l):
    if a[i] > b[i]:
        ans = 1
        break
    elif a[i] < b[i]:
        ans = -1
        break
    else:
        continue

print(ans)
