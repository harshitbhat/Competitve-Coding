# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

def kthLargestValue(matrix,k):
    rowMat = []
    colMat1 = []
    for row in matrix:
        temp = []
        temp.append(row[0])
        for i in range(1,len(row)):
            temp.append(row[i]^temp[i-1])
        rowMat.append(temp)
    for i in range(0,len(matrix[0])):
        temp = []
        temp.append(matrix[0][i])
        for j in range(1,len(matrix)):
            temp.append(temp[j-1]^matrix[j][i])
        colMat1.append(temp)
    colMat = []
    for i in range(len(colMat1[0])):
        temp = []
        for j in range(len(colMat1)):
            temp.append(colMat1[j][i])
        colMat.append(temp)

    m = len(matrix)
    n = len(matrix[0])
    ans = matrix
    # print(m,n,rowMat,colMat)
    for i in range(0,n):
        ans[0][i] = rowMat[0][i]
    for i in range(0,m):
        ans[i][0] = colMat[i][0]
    for i in range(1,m):
        for j in range(1,n):
            ans[i][j] = ans[i][j] ^ ans[i-1][j-1] ^ colMat[i-1][j] ^ rowMat[i][j-1]

    kth = []
    for i in range(0,m):
        for j in range(0,n):
            kth.append(ans[i][j])
    
    kth.sort(reverse=True)
    # print(kth)
    return(kth[k-1])
    





kthLargestValue([[5,2],[1,6]],1)
# kthLargestValue([[3,4,1,2,3],[7,8,5,1,2],[1,6,5,2,4],[9,7,1,2,3]],2)