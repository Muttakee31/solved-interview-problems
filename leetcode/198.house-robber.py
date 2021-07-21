class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/house-robber/
        """
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[-1]