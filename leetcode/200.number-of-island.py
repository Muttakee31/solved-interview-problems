class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        https://leetcode.com/problems/number-of-islands/
        its similar to counting graphs in a forest.
        """
        m, n = len(grid), len(grid[0])
        island = 0
        ones = sum(x.count('1') for x in grid)
        visited = [[0]*n for i in range(m)]
        
        def dfs(i:int, j:int):
            visited[i][j] = 1
            if i != 0 and grid[i-1][j] == '1' and visited[i-1][j] == 0:
                dfs(i-1, j)
            if j != 0 and grid[i][j-1] == '1' and visited[i][j-1] == 0:
                dfs(i, j-1)
            if i != m-1 and grid[i+1][j] == '1' and visited[i+1][j] == 0:
                dfs(i+1, j)
            if j != n-1 and grid[i][j+1] == '1' and visited[i][j+1] == 0:
                dfs(i, j+1)

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    dfs(i,j)
                    island += 1

        return island