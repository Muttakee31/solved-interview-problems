from classes.TreeNode import TreeNode

class Solution:
    diameter = 0
    def dfs(self, node:TreeNode, depth:int)-> int:
        if not node:
            return 0
        p = self.dfs(node.left, depth + 1)
        q = self.dfs(node.right, depth + 1)
        self.diameter = max(self.diameter, p + q)
        return 1 + max(p,q)
                    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.diameter