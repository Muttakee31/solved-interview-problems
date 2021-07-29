from classes.TreeNode import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/sum-of-left-leaves/
        """
        sum = 0
        q = list()
        q.append(root)
        while(len(q) != 0):
            first = q.pop(0)
            if first.left:
                if first.left.left is None and first.left.right is None:
                    sum += first.left.val
                q.append(first.left)
            if first.right:
                q.append(first.right)
        
        return sum