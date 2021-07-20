class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        """
         https://leetcode.com/problems/valid-perfect-square/
         two different solutions
         i = 1
         while(i*i<n):
             i+=1
        
        return True if i*i == n else False
        """ 
        low = 1
        high = n
        
        while(low <= high):
            mid = (low + high) // 2
            if mid*mid == n:
                return True
            if mid*mid > high:
                high = mid-1
            else:
                low = mid + 1
            
        return False