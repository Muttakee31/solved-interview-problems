class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/triangle/
        use dp. start from the bottom row.
        """
        n = len(triangle)
        dp = [[0]*len(triangle[i]) for i in range(n)]
        dp[-1] = triangle[-1]
        print(dp)
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = min(triangle[i][j] + dp[i+1][j], triangle[i][j] + dp[i+1][j+1])
            
        return dp[0][0]