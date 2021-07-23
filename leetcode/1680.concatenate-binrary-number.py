class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
        """
        s = ''
        for i in range(n+1):
            s += "{0:b}".format(i)
        
        x = int(s, 2) % (10**9+7)
        return x

        """
        the original solution should be this
        def concatenatedBinary(self, n):
        ans, M = 0, 10**9 + 7
        for x in range(n):
            ans = (ans * (1 << (len(bin(x+1)) - 2)) + x+1) % M
        return ans 
        """