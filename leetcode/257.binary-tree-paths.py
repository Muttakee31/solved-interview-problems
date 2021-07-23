from classes.TreeNode import TreeNode

class Solution:
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        def generatePath(node: TreeNode, path: str):
            x = path + '->' + str(node.val)
            if node.left is None and node.right is None:
                ans.append(x[2:])
            if node.left:
                generatePath(node.left, x)
            if node.right:
                generatePath(node.right, x)

        if root is None:
            return []
        generatePath(root, '')
        return ans