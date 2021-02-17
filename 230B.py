import math
def isPrime(n):
    if n == 1:
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
    
def check(n):
    if n == 1:
        return False
    return math.floor(math.sqrt(n)) == math.ceil(math.sqrt(n)) and isPrime(int(math.sqrt(n)))
n = int(input())
arr = list(map(int,input().split()))
for i in arr:
    if check(i):
        print('YES')
    else:
        print('NO')