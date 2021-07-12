class Solution(object):
    def findDuplicate(self, nums):
        """
        learned floyd cycle detection. had no idea this can solved like this.
        """
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if hare == tortoise:
                break
        
        tortoise = nums[0]
        while hare != tortoise:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare