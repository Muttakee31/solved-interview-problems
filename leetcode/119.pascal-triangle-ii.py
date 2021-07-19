class Solution(object):
    def getRow(self, rowIndex):
        """
        https://leetcode.com/problems/pascals-triangle-ii/
        """
        li = []
        x = l = 1
        for i in range(0, rowIndex+1):
            li.append(x/l)
            x *= (rowIndex-i)
            l *= i+1        
        # li += li[0:rowIndex//2+rowIndex%2][::-1]
        return li