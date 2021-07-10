def solution(A, K):
    # write your code in Python 3.6
    def reverse(A, index, limit):
    	i=0
    	while (i < (limit - index)/2):
            A[index+i], A[limit-i-1] = A[limit-i-1], A[index+i]
            i += 1
    if len(A) == 0:
        return A
    
    K = K % len(A)

    reverse(A, 0, len(A))
    reverse(A, 0, K)
    reverse(A, K, len(A))
    return A