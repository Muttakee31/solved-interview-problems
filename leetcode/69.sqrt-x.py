def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    low = 0
    high = x
    mid = (low+high)/2
    while (low <= high):
        mid = (low+high)//2
        if abs(x - mid * mid) < 0.99:
            break
        if mid*mid > x:
            low = mid+1
        else:
            high = mid-1
    return mid
    
print(mySqrt(14))