class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/number-of-provinces/
        """
        n = len(isConnected)
        visited = [0]*n
        
        def dfs(i:int) -> None:
            visited[i] = 1
            for k in range(n):
                if isConnected[i][k] == 1 and k != i and visited[k] == 0:
                    dfs(k)

            
        count = 0
        for i in range(n):
            if visited[i] == 0:
                count += 1
                dfs(i)
            
        return count