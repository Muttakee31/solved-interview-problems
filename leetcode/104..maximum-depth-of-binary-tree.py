# Definition for a binary tree node.
class Solution(object):
    def dfs(self, node, depth):
        if node:
            p = self.dfs(node.left, depth+1)
            q = self.dfs(node.right, depth+1)
            return max(p, q)
        return depth
        
    def maxDepth(self, root):
        """
        https://leetcode.com/problems/maximum-depth-of-binary-tree/
        used dfs to calculate and return the max depth to top
        """
        return self.dfs(root, 0)