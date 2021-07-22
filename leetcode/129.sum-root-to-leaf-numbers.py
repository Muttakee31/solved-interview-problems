from classes.TreeNode import TreeNode


class Solution:
    TreeNode : TreeNode
    def pathSum(self, node:TreeNode, sum:int)->int:
        p = q = 0
        if node.left:
            p = self.pathSum(node.left, sum * 10 + node.val)
        if node.right:
            q = self.pathSum(node.right, sum * 10 + node.val)
        
        if node.left is None and node.right is None:
            return node.val + sum * 10
        return p + q
    
    def sumNumbers(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/sum-root-to-leaf-numbers/
        """
        if root is None:
            return 0
        return self.pathSum(root, 0)