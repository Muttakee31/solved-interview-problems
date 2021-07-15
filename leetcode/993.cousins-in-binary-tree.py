class Solution(object):
    dx = dy = xparent = yparent = None
    def calculateHeight(self, node, x, y, parent=None, index=0):
        global dx
        global dy
        global xparent
        global yparent
        if node is not None:
            if node.val == x:
                dx = index
                xparent = parent
            if node.val == y:
                dy = index
                yparent = parent
            self.calculateHeight(node.left, x, y, node, index+1)
            self.calculateHeight(node.right, x, y, node, index+1)
        else:
            return None
        
    def isCousins(self, root, x, y):
        """
        https://leetcode.com/problems/cousins-in-binary-tree/
        saved the depth and parent of x and y in a global variable.
        then checked if the condition is fine or not
        """
        self.calculateHeight(root, x, y)
        if dx == dy and xparent and yparent and xparent != yparent:
            return True
        else:
            return False
