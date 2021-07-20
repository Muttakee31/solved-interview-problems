class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
        """
        nums.sort(key = lambda x: abs(x))
        return [x*x for x in nums]