def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n %3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

T = int(input())
while T > 0:
    T = T - 1
    diff = int(input())
    a = 1
    b = a + diff
    if b % 2 == 0 and diff != 1:
        b += 1
    while True:
        if isPrime(b) and (b-a) >= diff:
            break
        b += 2
    c = b + diff
    if c % 2 == 0:
        c += 1
    while True:
        if isPrime(c) and (c-b) >= diff:
            break
        c += 2
    print(b*c)
