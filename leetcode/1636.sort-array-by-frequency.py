from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/sort-array-by-increasing-frequency/
        calculate the count. then sort them using lambda function.
        """
        counter = list(Counter(nums).items())
        counter.sort(key = lambda x: (x[1], -x[0]))
        li = []
        for c in counter:
            li += [c[0]] * c[1]
        
        return li