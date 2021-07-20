class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/product-of-array-except-self/
        calculate cumulative product from start and end.
        Then use them to calculate the result.
        """
        n = len(nums)
        front = [0]*n
        back = [0]*n
        front[0] = nums[0]
        back[-1] = nums[-1]
        for i in range(1, n):
            front[i] = front[i-1]*nums[i]
            back[-i-1] = back[-i]*nums[-i-1]
        # print(front)
        # print(back)
        res = [0]*n
        res[0] = back[1]
        res[-1] = front[-2]
        for i in range(1,n-1):
            res[i] = front[i-1] * back[i+1]
        return res