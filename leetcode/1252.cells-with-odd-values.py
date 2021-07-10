"""
solved myself yayyy!!
"""
class Solution(object):
    def oddCells(self, m, n, indices):
        total = 0
        odd_row = 0
        odd_col = 0
        row_flag = [-1 for i in range(m)]
        col_flag = [-1 for i in range(n)]
        for ind in indices:
            row_flag[ind[0]] *= -1
            col_flag[ind[1]] *= -1
        
        for r in row_flag:
            if r == 1:
                total += n
                odd_row += 1
                
        for c in col_flag:
            if c == 1:
                total += m - 2 * odd_row
        
        return total
