def reverse(num):
    dup = 0
    while num > 0:
        dup = dup * 10 + num % 10
        num = int(num/10)
    return dup

t = int(input())
while t>0:
    t = t-1
    a,b = map(int,input().split())
    print(reverse(reverse(a) + reverse(b)))