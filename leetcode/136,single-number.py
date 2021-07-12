class Solution(object):
    def singleNumber(self, nums):
        """
        used codility solution for odd-occurance. though later realized the problem is easier.
        """
        hash = dict()
        for num in nums:
            if num not in hash.keys():
                hash[num] = 1
            else:
                hash[num] *= -1

        for key, value in hash.items():
            if value == 1:
                return key

        """
        return 2 * sum(set(nums)) - sum(nums)
        """