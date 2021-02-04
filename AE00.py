def numberOfFactors(n):
    nums = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            if int(n / i) == i:
                nums = nums + 1
            else:
                nums = nums + 2
        i = i + 1
    return nums

n = int(input())

squares = []
i = 1
while i*i <= 10001:
    squares.append(i*i)
    i = i + 1
arr = []
arr.append(0)
arr.append(1)
arr.append(2)
arr.append(3)
for i in range(4,n+1):
    facs = numberOfFactors(i)
    if facs == 2:
        arr.append(arr[i-1] + 1)
    elif i in squares:
        facs -= 3
        arr.append(arr[i-1] + 1 + 1 + int(facs/2))
    else:
        facs -= 2
        arr.append(arr[i-1] + 1 + int(facs/2))
print(arr[n])