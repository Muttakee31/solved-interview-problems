def solution(A):
    # write your code in Python 3.6
    l = len(A)
    sum = [0 for i in range(l)]
    rev_sum = [0 for i in range(l)]
    sum[0] = A[0]
    rev_sum[l-1] = A[l-1]
    for i in range(1, len(A)):
        sum[i] = sum[i-1] + A[i]

    for i in range(l-2, -1, -1):
        rev_sum[i] = rev_sum[i+1] + A[i]
    
    min = float('inf')
    for i in range(0, l-1):
        x = abs(sum[i] - rev_sum[i+1])
        if x < min:
            min = x
    
    return min