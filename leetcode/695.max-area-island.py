class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/max-area-of-island/
        call dfs and add the grids with 1.
        """
        m, n = len(grid), len(grid[0])
        big_island = 0
        ones = sum(x.count(1) for x in grid)
        visited = [[0]*n for i in range(m)]
        
        def dfs(i:int, j:int) -> int:
            p = 1
            visited[i][j] = 1
            if i != 0 and grid[i-1][j] == 1 and visited[i-1][j] == 0:
                p += dfs(i-1, j)
            if j != 0 and grid[i][j-1] == 1 and visited[i][j-1] == 0:
                p += dfs(i, j-1)
            if i != m-1 and grid[i+1][j] == 1 and visited[i+1][j] == 0:
                p += dfs(i+1, j)
            if j != n-1 and grid[i][j+1] == 1 and visited[i][j+1] == 0:
                p += dfs(i, j+1)
            return p

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    p = dfs(i,j)
                    big_island = max(big_island, p)

        return big_island