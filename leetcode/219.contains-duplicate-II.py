class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        https://leetcode.com/problems/contains-duplicate-ii/
        store the index in the dictionary with value as key.
        check if the index previously saved is less than or equal k or not
        """
        danger = dict()
        if len(nums) <= 1 or len(set(nums)) == len(nums):
            return False
        for i in range(len(nums)):
            if nums[i] in danger.keys() and i - danger[nums[i]] <= k:
                return True
            danger[nums[i]] = i
        return False