import math

def simpleSieve(limit):
    mark = [True] * (limit + 1)
    mark[0] = mark[1] = False
    i = 2
    primes = []
    while i*i <= limit:
        if mark[i] == True:
            j = 2 * i
            while j <= limit:
                mark[j] = False
                j = j + i
        i = i + 1
    for i in range(0,limit+1):
        if mark[i] == True:
            primes.append(i)
    return primes
    
def primeInRange(low,high):
    limit = int(math.sqrt(high)) + 1
    primes = simpleSieve(limit)
    
    n = high - low + 1
    mark = [True] * (n+1)
    l = len(primes)

    for i in range(l):
        lowLimit = int(low/primes[i]) * primes[i]
        if lowLimit < low or lowLimit == primes[i]:
            lowLimit = lowLimit + primes[i]
        for j in range(lowLimit,high+1,primes[i]):
            if j != primes[i]:
                mark[j-low] = False
    
    for i in range(low,high+1):
        if mark[i-low] == True and i != 1:
            print(i)
    
t = int(input())
while t>0:
    t = t-1
    m,n = map(int,input().split())
    primeInRange(m,n)
    print()