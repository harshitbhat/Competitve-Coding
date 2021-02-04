import math

def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
primes = []
for i in range(2,1000):
    if isPrime(i) == True:
        primes.append(i)

def diffFactors(n):
    noOfPrimeFactors = 0
    for i in range(0,len(primes)):
        if n % primes[i] == 0:
            noOfPrimeFactors += 1
            while n % primes[i] == 0:
                n = int(n/primes[i])
    return noOfPrimeFactors

luckyNums = []
counter = 0
init = 30
while counter <= 1001:
    if diffFactors(init) >= 3:
        luckyNums.append(init)
        counter += 1
    init += 1

T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    print(luckyNums[n-1])
