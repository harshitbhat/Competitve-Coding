def check(arr):
    stk = []
    for i in arr:
        if i == '(':
            stk.append(i)
        else:
            if not stk:
                return False
            stk.pop()

    return len(stk) == 0

T = int(input())
while T > 0:
    T = T - 1
    s = input()
    possible = ['(',')']
    charA = charB = charC = ''
    isPositive = False
    for i in possible:
        charA = i
        for j in possible:
            charB = j
            for k in possible:
                charC = k
                b = []
                for elem in s:
                    if elem == 'A':
                        b.append(charA)
                    if elem == 'B':
                        b.append(charB)
                    if elem == 'C':
                        b.append(charC)
                isPositive = check(b)
                if isPositive:
                    break
            if isPositive:
                break
        if isPositive:
            break
    if isPositive:
        print('YES')
    else:
        print('NO')