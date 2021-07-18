from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        https://leetcode.com/problems/valid-anagram/
        """
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2