from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        """
        https://leetcode.com/problems/sort-characters-by-frequency/
        sort after counting number of elements and build the string.
        """
        co = Counter(s)
        co = list(co.items())
        co.sort(key=lambda x: -x[1])
        
        ans = ''
        for t in co:
            ans += t[0]*t[1]
        return ans