class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/house-robber-ii/
        solution is cool. could not solve.
        solve the problem for 1 to n-1 house and 2 to n indexed house.
        max of these two subproblem holds the answer.
        """
        n = len(nums)
        if n==1:
            return nums[0]
        dp = [0 for i in range(n-1)]
        dp[0] = nums[0]
        for i in range(1, n-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        new_dp = [0 for i in range(n-1)]
        new_dp[0] = nums[1]
        for i in range(1, n-1):
            new_dp[i] = max(new_dp[i-1], new_dp[i-2]+nums[i+1])
        return dp[n-2] if dp[n-2] > new_dp[n-2] else new_dp[n-2]