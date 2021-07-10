def solution(N):
    max_distance = count = 0
    ones = []
    i = 0
    while (N > 0):
        if (N % 2 == 1):
            ones.append(i)
        i+=1
        N //= 2
    for k in range(1, len(ones)):
        max_distance = max(max_distance, ones[k] - ones[k-1] -1)
    return max_distance