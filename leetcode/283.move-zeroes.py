class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = count = 0
        l = len(nums)
        for n in range(l):
            if nums[n] != 0:
                nums[i] = nums[n]
                i+=1
            else:
                count += 1
        for x in range(count):
            nums[l-x-1] = 0

        