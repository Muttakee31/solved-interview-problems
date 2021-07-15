class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        https://leetcode.com/problems/excel-sheet-column-number/
        26-base conversion to number does the trick here
        """
        p = 1
        x = 0
        for i in range(len(columnTitle)-1, -1, -1):
            c = ord(columnTitle[i]) - 64
            x = x + c * p
            p *= 26
        
        return x