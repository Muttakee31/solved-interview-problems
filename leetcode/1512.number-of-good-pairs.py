from collections import Counter

class Solution:
    """
    https://leetcode.com/problems/number-of-good-pairs/
    how to pick two numbers from n found from counter.
    """
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        pairs = 0
        for value in counter.values():
            if value > 1:
                pairs += (value * (value-1))//2
        
        return pairs