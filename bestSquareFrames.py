def bestSquareFrames(matrix,frameSize):
    n = len(matrix)
    m = len(matrix[0])
    ans = []
    for i in range(n - frameSize + 1):
        for j in range(m - frameSize + 1):
            mat = []
            for x in range(i, frameSize + i):
                for y in range(j, frameSize + j):
                    if x == i or x == (i + frameSize - 1):
                        mat.append(matrix[x][y])
                    else:
                        if y == j or y == (j + frameSize - 1):
                            mat.append(matrix[x][y])
            ans.append(mat)
    maxSum = -1
    for a in ans:
        maxSum = max(maxSum,sum(a))
    tempArr = []
    for a in ans:
        if sum(a) == maxSum:
            for i in a:
                tempArr.append(i)
    mySet = set(tempArr)
    return sum(mySet)


matrix = [[9,  7,  8,  9,  2],
          [6,  9,  9,  6,  1],
          [4,  10, 1,  3,  10],
          [18,  2,  3,  9,  3],
          [4,  6,  8,  5,  21]]

temp = bestSquareFrames(matrix,3)
print(temp)