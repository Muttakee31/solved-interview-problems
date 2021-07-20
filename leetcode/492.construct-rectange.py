import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        https://leetcode.com/problems/construct-the-rectangle/
        """
        root = math.floor(math.sqrt(area))
        while(root>0):
            if area % root == 0:
                return [area//root, root]
            root -= 1