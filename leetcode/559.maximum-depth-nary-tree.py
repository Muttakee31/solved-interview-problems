class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    """
    https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
    """
    def getDepth(self, node:'Node', depth:int) -> int:
        m = depth+1
        for c in node.children:
            m = max(m ,self.getDepth(c, depth+1))
        return m
        
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        return self.getDepth(root, 0)