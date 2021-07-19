from collections import List

class Solution(object):
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/find-all-duplicates-in-an-array/
        """
        rs = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                rs.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return rs

        """
        my solution sucks. I tried the above solution but something went wrong :(
        class Solution(object):
        def findDuplicates(self, nums):
            mask = 1000000
            for i in range(len(nums)):
                m = abs(nums[i]) % mask - 1
                if abs(nums[m]) < mask:
                    nums[m] += mask
                nums[m] = nums[m] * -1
                
            li = []
            # print(nums)
            for i in range(len(nums)):
                if nums[i] > 0 and nums[i] > mask:
                    li.append(i+1)
            return li
        """