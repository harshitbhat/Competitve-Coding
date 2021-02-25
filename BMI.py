T = int(input())
for i in range(T):
    m,h = map(int,input().split())
    bmi = m // (h**2)
    cat = 1
    if bmi <= 18:
        cat = 1
    elif bmi <= 24:
        cat = 2
    elif bmi <= 29:
        cat = 3
    else:
        cat = 4
    print(cat)