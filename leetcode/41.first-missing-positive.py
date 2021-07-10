# missed solution  completely. needed help.
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        contains_one = False
        num_len = len(nums)
        for i in range(num_len):
            if nums[i] == 1:
                contains_one = True
        if not contains_one:
            return 1
        if (num_len == 1):
            return 2
        
        for i in range(num_len):
            if (nums[i] > num_len or nums[i] <= 0):
                nums[i] = 1
        
        for i in range(num_len):
            x = abs(nums[i])
            if (nums[x-1] > 0):
                nums[x-1] *= -1
        
        for i in range(num_len):
            if (nums[i] > 0):
                return i + 1
        
        return num_len + 1

