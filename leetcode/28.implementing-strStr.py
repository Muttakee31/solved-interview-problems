class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nl = len(needle)
        if nl == 0:
            return 0
        
        for i in range(0, len(haystack)-nl):
            if haystack[i:i+nl] == needle:
                return i
        
        return -1
        