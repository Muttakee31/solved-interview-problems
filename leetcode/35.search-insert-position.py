class Solution(object):
    def searchInsert(self, nums, target):
        """
        https://leetcode.com/problems/search-insert-position/
        binary search problem. needed help as i was using wrong mid value in conditions.
        """
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        low = 0
        high = len(nums)-1
        
        while(low<=high):
            mid = (low+high)//2
            if target > nums[mid-1] and target<= nums[mid]:
                break
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
            # print(mid)
        
        return mid