class Solution:
    """
    https://leetcode.com/problems/reverse-bits/

    """
    def reverseBits(self, n: int) -> int:
        p = c = 0
        while (n):
            x = n%2
            p = p<<1 | x
            # or, ret += (n & 1) << power
            n = n >> 1
            c += 1
        for i in range(c, 32):
            p = p<<1
        return p