class Solution(object):
    def missingNumber(self, nums):
        """
        https://leetcode.com/problems/missing-number/
        no regret watching the solution for a peak. XOR to the rescue. xor all index and the array values.
        then xor the two values to get the missing number.
        """
        index_xor = 0
        value_xor = 0
        for i in range(len(nums)):
            index_xor ^= i+1
            value_xor ^= nums[i]
        
        
        
        return index_xor ^ value_xor