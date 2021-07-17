from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        https://leetcode.com/problems/first-unique-character-in-a-string/
        ise counter then iterate the string to check which element appears first with count 1.
        """
        co = Counter(s)
        # print(co)
        for i, c in enumerate(s):
            if co[c] == 1:
                return i
        return -1
        