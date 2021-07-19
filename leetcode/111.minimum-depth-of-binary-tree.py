class Solution(object):
    def dfs(self, node, depth):
        if node.left and node.right:
            p = self.dfs(node.left, depth+1)
            q = self.dfs(node.right, depth+1)
            return min(p, q)
        elif node.right is None and node.left is not None:
            return self.dfs(node.left, depth + 1)
        elif node.right is not None and node.left is None:
            return self.dfs(node.right, depth+1)
        else:
            return depth
        
    def minDepth(self, root):
        """
        https://leetcode.com/problems/minimum-depth-of-binary-tree/
        """
        return self.dfs(root, 1) if root is not None else 0
        
        """
        below is the bfs solution. return the first leaf. way simple than my dfs :(
        def minDepth(self, root):
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1)
        """