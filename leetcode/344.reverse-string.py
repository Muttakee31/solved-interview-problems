class Solution(object):
    def reverseString(self, s):
        """
        https://leetcode.com/problems/reverse-string/
        reverse string
        """
        for i in range(len(s)/2):
            s[i], s[-i-1] = s[-i-1], s[i]
