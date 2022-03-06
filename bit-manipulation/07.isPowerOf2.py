def isPowerOf2(n):
    if n == 0:
        return False
    
    while n != 1:
        if n % 2 != 0:
            return False
        
        n = n >> 1
    
    return True


# ---------------------------------------------------------------------------- #
#                          Brian Kernighan’s algorithm                         #
# ---------------------------------------------------------------------------- #

def isPowerOfTwo(n):
    return n != 0 and n & (n - 1) == 0


num = 62

print(f'Is {num} power of 2: {isPowerOf2(num)}')
print(f'Is {num} power of 2: {isPowerOfTwo(num)}')