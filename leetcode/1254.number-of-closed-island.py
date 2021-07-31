class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/number-of-closed-islands
        well flags were not declared as it should be.
        loops needed more strict range. my bad.
        """
        m, n = len(grid), len(grid[0])
        island = 0
        
        def dfs(i:int, j:int) -> bool:
            if grid[i][j] == 1:
                return True
            if (i == 0 or i == m-1 or j == 0 or j == n-1):
                return False
            grid[i][j] = 1
            a = dfs(i-1, j)
            b = dfs(i, j-1)
            c = dfs(i+1, j)
            d = dfs(i, j+1)
            return a and b and c and d

        for i in range(1, m-1):
            for j in range(1,  n-1):
                if grid[i][j] == 0 and dfs(i,j):
                    island += 1
        return island