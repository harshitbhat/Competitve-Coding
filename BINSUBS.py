def longest_non_decreasing_subsequence(arr):
    
    N = len(arr)
    P = [0] * N
    M = [0] * (N+1)
    L = 0
    for i in range(N):
       lo = 1
       hi = L
       while lo <= hi:
           mid = (lo+hi)//2
           if (arr[M[mid]] <= arr[i]):
               lo = mid+1
           else:
               hi = mid-1
 
       newL = lo
       P[i] = M[newL-1]
       M[newL] = i
 
       if (newL > L):
           L = newL
 
    subsequence = []
    k = M[L]
    for i in range(L-1, -1, -1):
        subsequence.append(arr[k])
        k = P[k]
    return len(subsequence)

T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    s = input()
    arr = [int(i) for i in s]
    print(n - longest_non_decreasing_subsequence(arr))