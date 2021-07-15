class Solution(object):
    def isPowerOfThree(self, n):
        """
        https://leetcode.com/problems/power-of-three/
        alternate solution is to convert the number to base three and match pattern with ^10*$
        """
        if n < 1:
            return False
        while(n % 3 == 0):
            n /= 3
        
        return True if n == 1 else False