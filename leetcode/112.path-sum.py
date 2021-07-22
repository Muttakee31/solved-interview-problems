class Solution:
    def pathSum(self, node, sum, targetSum):
        p = q = False
        if node.left:
            p = self.pathSum(node.left, sum + node.val, targetSum)
        if node.right:
            q = self.pathSum(node.right, sum + node.val, targetSum)
        
        if node.left is None and node.right is None:
            # print(node.val + sum)
            # return node.val + sum
            if node.val + sum == targetSum:
                return True
            else:
                return False
        return (p or q)
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        https://leetcode.com/problems/path-sum/
        """
        if root is None:
            return False
        return self.pathSum(root, 0, targetSum)