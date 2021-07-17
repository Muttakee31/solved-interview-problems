class Solution(object):
    def reverse(self, A, index, limit):
    	i=0
    	while (i < (limit - index)/2):
            A[index+i], A[limit-i-1] = A[limit-i-1], A[index+i]
            i += 1
            
    def rotate(self, nums, k):
        """
        did this one in codility before
        """
        if len(nums) == 0:
            return nums
    
        k = k % len(nums)

        self.reverse(nums, 0, len(nums))
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))