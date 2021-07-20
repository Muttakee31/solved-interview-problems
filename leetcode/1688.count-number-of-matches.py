class Solution:
    def numberOfMatches(self, n: int) -> int:
        """
        https://leetcode.com/problems/count-of-matches-in-tournament/
        """
        count = 0
        while(n>1):
            count+=n//2
            n = n//2 + n%2

        return count