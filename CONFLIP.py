T = int(input())
for j in range(T):
    G = int(input())
    for i in range(G):
        I , N, Q = map(int,input().split())
        H = T = 0
        if N % 2 == 0:
            H = T = N // 2
        else:
            if I == 1:
                H = N // 2
                T = H + 1
            else:
                T = N // 2
                H = T + 1
        if Q == 1:
            print(H)
        else:
            print(T)