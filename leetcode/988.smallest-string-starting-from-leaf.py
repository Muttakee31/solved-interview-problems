class Solution:
    ans = '~'
    
    def pathSum(self, node: TreeNode, s:str):
        c = chr(node.val+97)
        s += c

        if node.left is None and node.right is None:
            self.ans = min(self.ans, "".join(reversed(s)))
        if node.left:
            self.pathSum(node.left, s)
        if node.right:
            self.pathSum(node.right, s)
        # print(self.ans)
        s = s[:-1]
    
    def smallestFromLeaf(self, root: TreeNode) -> bool:
        """
        https://leetcode.com/problems/smallest-string-starting-from-leaf/
        needed to save the string in a global variable.
        """
        if root is None:
            return False
        self.pathSum(root, '')
        return self.ans