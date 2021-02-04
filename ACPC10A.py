while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if b - a == c - b:
            print(f"AP {c + (b-a)}")
        else:
            print(f"GP {c * int(b/a)}")