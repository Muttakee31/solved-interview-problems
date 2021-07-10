def solution(A):
    # write your code in Python 3.6
    hash = dict()
    for num in A:
        if num not in hash.keys():
            A[num] = 1
        else:
            A[num] *= -1
    
    for key, value in hash.items():
        if value == 1:
            return key