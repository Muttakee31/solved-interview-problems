class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/kth-largest-element-in-an-array/
        """
        # nums = list(set(nums))
        nums.sort(reverse=True)
        return nums[k-1]