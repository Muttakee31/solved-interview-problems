class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/third-maximum-number/
        """
        first = second = third = float('-inf')
        
        for i in range(len(nums)):
            if nums[i] > first:
                third = second
                second = first
                first = nums[i]
            elif nums[i] > second and nums[i] < first:
                third = second
                second = nums[i]
            elif nums[i] > third and nums[i] < second:
                third = nums[i]    
            # print(str(first) + "    " + str(second) + "    " + str(third))
        return third if third != float('-inf') else first