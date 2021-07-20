class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        https://leetcode.com/problems/bulb-switcher/
        """
        if n == 0:
            return 0
        i = 1
        while(i*i<=n):
            i+=1
        return i-1