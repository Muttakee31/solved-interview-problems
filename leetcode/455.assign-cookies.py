class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        https://leetcode.com/problems/assign-cookies/
        """
        i = j = count = 0
        m, n = len(g), len(s)
        g.sort()
        s.sort()
        while i < m and j < n:
            if g[i] <= s[j]:
                count += 1
                i += 1
            j += 1
        
        return count