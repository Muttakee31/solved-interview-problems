class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 5
        count = 0
        if n == 0:
            return 0
        while (n >= p):
            count += n // p
            p *= 5
        
        return count
