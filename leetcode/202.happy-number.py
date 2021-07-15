class Solution(object):
    def sumsquare(self, n):
        sum = 0
        while(n > 0):
            p = n % 10
            sum += p ** 2
            n //= 10
        return sum
    
    def isHappy(self, n):
        """
        https://leetcode.com/problems/happy-number/
        could use simple hashmap.
        but floyd cycle detection to the rescue.
        mathematically there will always be a cycle in a pattern like this
        just detect the cycle and check if the cycle is in 1 or not and voila!
        """
        slow = self.sumsquare(n)
        fast = self.sumsquare(slow)
        while (True):
            if slow == fast:
                break
            slow = self.sumsquare(slow)
            fast = self.sumsquare(self.sumsquare(fast))
        
        return fast == 1
            