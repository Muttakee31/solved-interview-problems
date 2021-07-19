class Solution(object):
    def guessNumber(self, n):
        """
        https://leetcode.com/problems/guess-number-higher-or-lower/
        another binary search
        """
        low = 1
        high = n
        
        while(low <= high):
            mid = (low+high)//2
            f = guess(mid)
            if f==0:
                break
            elif f==-1:
                high = mid - 1
            else:
                low = mid + 1
            # print(mid)
        return mid