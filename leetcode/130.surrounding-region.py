class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def dfs(i:int, j:int) -> None:
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                return
            if board[i][j] == 'O':
                board[i][j] = 'P'
                dfs(i-1, j)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i, j+1)


        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        
        for i in range(1, n-1):
            dfs(0, i)
            dfs(m-1, i)
        
        for i in range(0, m):
            for j in range(0,  n):
                if board[i][j] == 'P':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'