class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        https://leetcode.com/problems/sort-colors/
        Shift all zeroes to left. then shift all ones left.
        """
        last_zero = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                if last_zero > i:
                    last_zero = i + 1
                else:
                    nums[i], nums[last_zero] = nums[last_zero], nums[i]
                    last_zero += 1
            
        # print(nums)
        for i in range(last_zero, n):
             if nums[i] == 1:
                if last_zero > i:
                    last_zero = i + 1
                else:
                    nums[i], nums[last_zero] = nums[last_zero], nums[i]
                    last_zero += 1
        # print(nums)
        return nums