def fact(n):
    res = [0] * 201
    res[0] = 1
    i = 1
    while i<=n:
        carry = 0
        j = 0
        while j <= 200:
            z = res[j] * i
            val = z + carry
            res[j] = val % 10
            carry = int(val/10)
            j = j + 1
        i = i + 1
    k = 200
    i = 200
    while i >= 0:
        if res[i] != 0:
            k = i
            break
        i = i - 1
    i = k
    while i>=0:
        print(res[i],end="")
        i = i - 1
    print()

t = int(input())
while t > 0:
    t = t - 1
    n = int(input())
    fact(n)