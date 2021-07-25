class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/longest-increasing-subsequence/
        missed by a mile. -_-
        the concept is to calculate the number of values smaller than the i-th value.
        """
        n = len(nums)
        dp = [1]*n
        
        for i in range(n):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
        return max(dp)