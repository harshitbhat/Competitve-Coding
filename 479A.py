def calcMax(a,b,c):
    arr = []
    arr.append((a+b)+c)
    arr.append((a+b)*c)
    arr.append((a*b)+c)
    arr.append((a*b)*c)
    arr.append(a+(b+c))
    arr.append(a+(b*c))
    arr.append(a*(b+c))
    arr.append(a*(b*c))
    arr.sort()
    return arr[len(arr) - 1]

a = int(input())
b = int(input())
c = int(input())
print(calcMax(a,b,c))