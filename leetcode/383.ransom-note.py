from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        https://leetcode.com/problems/ransom-note/
        """
        r = Counter(ransomNote)
        m = Counter(magazine)
        
        for k in r.keys():
            # print(k + "   " + str(m[k]) + '  ' + str(r[k]))
            if m[k] < r[k]:
                return False
        
        return True