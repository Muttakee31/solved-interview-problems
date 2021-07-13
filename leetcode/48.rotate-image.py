def rotate(self, matrix):
        """
        https://leetcode.com/problems/rotate-image/
        failed to solve :(
        first transpose the matrix, then reverse the matrix.
        """
        n = len(matrix[0])-1
        
        for i in range(n+1):
            for j in range(i, n + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n+1):
            for j in range((n+1)//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]