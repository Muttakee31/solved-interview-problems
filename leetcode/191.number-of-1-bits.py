class Solution(object):
    def hammingWeight(self, n):
        """
        https://leetcode.com/problems/number-of-1-bits/
        this one is optimized. n & n-1 always flips least significant 1 bit.
        """
        c = 0
        while(n):
            c += 1   
            n = n & (n-1)
        return c