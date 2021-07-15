class Solution(object):
    """
    https://leetcode.com/problems/symmetric-tree/
    could not solve due to some weird bug. but the approach was okay.
    """
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.checkEquality(root.left, root.right)

    def checkEquality(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        outPair = self.checkEquality(left.left, right.right)
        inPair = self.checkEquality(left.right, right.left)
        return (left.val == right.val) and outPair and inPair