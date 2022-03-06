def countSetBit(n):
    ans = 0

    while n:
        n &= (n-1)
        ans += 1
    
    return ans

def countingBits(n):
    ans = []

    for i in range(n):
        ans.append(countSetBit(i + 1))
    
    return ans


print("Set bits of first n numbers: ", countingBits(6))