class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/maximum-length-of-pair-chain/
        """
        n = len(pairs)
        pairs.sort(key = lambda x: x[0])
        dp = [1]*n
        for i in range(n):
            for j in range(0,i):
                if pairs[i][0] > pairs[j][1] and dp[i] < dp[j] +1:
                    dp[i] = dp[j] + 1
        
        return max(dp)