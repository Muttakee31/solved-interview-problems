class Solution(object):
    def firstBadVersion(self, n):
        """
        https://leetcode.com/problems/first-bad-version/
        isBadVersion is already given. just needed to binary search to find the solution.
        """
        
        low = 1
        high = n
        
        if isBadVersion(1):
            return 1
        while(low <= high):
            mid = (low+high)//2
            f = isBadVersion(mid)
            g = isBadVersion(mid+1)
            if not f and g:
                break
            elif f:
                high = mid - 1
            else:
                low = mid + 1
            # print(mid)
        return mid+1