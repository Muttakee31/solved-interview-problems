class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/island-perimeter/
        """
        peri = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i != 0:
                        if grid[i-1][j] == 0:
                            peri += 1
                    else:
                        peri += 1
                    if j != 0:
                        if grid[i][j-1] == 0:
                            peri += 1
                    else:
                        peri += 1
                    if i != m-1:
                        if grid[i+1][j] == 0:
                            peri += 1
                    else:
                        peri += 1
                    if j != n-1:
                        if grid[i][j+1] == 0:
                            peri += 1
                    else:
                        peri += 1
        return peri
                    