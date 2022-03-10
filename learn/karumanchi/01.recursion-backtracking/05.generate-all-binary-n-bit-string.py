def appendAtBeginning(x , L):
    return [x + elem for elem in L]

def bitStrings(n):
    if n == 0:
        return []
    if n == 1:
        return ['0' , '1']
    
    return appendAtBeginning('0', bitStrings(n-1)) + appendAtBeginning('1', bitStrings(n-1))

print(bitStrings(3))