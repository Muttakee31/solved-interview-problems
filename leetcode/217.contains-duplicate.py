from collections import Counter


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        for c in count.values():
            if c > 1:
                return True
        return False
