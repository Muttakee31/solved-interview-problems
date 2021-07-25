class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if min(m,n) == 1:
            return 1
        p = m+n-2
        q = 1
        for i in range(1,n-1):
            q *= i+1
            p *= (m+n-2-i)
        return p//q