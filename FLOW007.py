def reverse(n):
    num = 0;
    x = n
    while x > 0:
        num = num * 10 + x % 10
        x = int(x / 10)
    return num

t = int(input())

while t>0:
    n = int(input())
    rev = reverse(n)
    print(rev)
    t = t-1