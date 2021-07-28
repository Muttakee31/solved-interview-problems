class Solution:
    def numDecodings(self, s: str) -> int:
        """
        https://leetcode.com/problems/decode-ways/
        """
        n = len(s)
        if s[0] == '0':
            return 0
        dp = [0]*(n+1)
        
        dp[0] = 1
        dp[1] = 0 if dp[0] == '0' else 1
        
        for i in range(2, n+1):
            if '0' < s[i-1] <= '9':
                dp[i] += dp[i-1]
            if '10' <= s[i-2] + s[i-1] <= '26':
                dp[i] += dp[i-2]
            
        return dp[n]