class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 2 * sum(set(nums)) - sum(nums)
        for n in nums:
            if p-n in nums:
                return [n, p-n]

        """"
        cooler bit manipulation solution. wish I could do this :/
        def singleNumber(self, nums: List[int]) -> List[int]:
            xor, res1, res2 = 0, 0, 0
            for num in nums:
                xor ^= num
            xor = xor & (~(xor-1))
            for num in nums:
                if num & xor == 0:
                    res1 ^= num
                else:
                    res2 ^= num

            return [res1, res2]
        """