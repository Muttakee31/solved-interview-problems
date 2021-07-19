from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        https://leetcode.com/problems/top-k-frequent-elements/

        """
        li = []
        co = Counter(nums).most_common(k)
        for c in co:
            li.append(c[0])
        return li