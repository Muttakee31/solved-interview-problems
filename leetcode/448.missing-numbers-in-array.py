class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
        """
        n = set(nums)
        li = list()
        for i in range(len(nums)):
            if i+1 not in n:
                li.append(i+1)
        
        return li

        """
        negate existing index.
        def findDisappearedNumbers(self, nums):
            for i in range(len(nums)):
                m = abs(nums[i]) - 1
                nums[m] = -nums[m] if nums[m]>0 else nums[m]
            
            li = []
            for i in range(len(nums)):
                if nums[i] > 0:
                    li.append(i+1)
        """