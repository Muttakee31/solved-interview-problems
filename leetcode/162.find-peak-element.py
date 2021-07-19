import random

class Solution(object):
    def findPeakElement(self, nums):
        """
        https://leetcode.com/problems/find-peak-element/
        worst solution to date.
        here is the OG recursive binary search solution
        class Solution:
    
        def search(self, nums: List[int], l:int, r:int) -> int:
            if l==r:
                return l
            mid = (l+r)//2
            if (nums[mid]>nums[mid+1]):
                return self.search(nums, l, mid)
            return self.search(nums, mid+1, r)
        
        def findPeakElement(self, nums: List[int]) -> int:
            return self.search(nums, 0, len(nums)-1)
        """
        
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))

        
        while(True):
            i = random.randint(1, len(nums)-2)
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                break
        
        return i-1