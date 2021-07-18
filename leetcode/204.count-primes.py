class Solution(object):
    def countPrimes(self, n):
        """
        https://leetcode.com/problems/count-primes/
        learned to write sieve finally. initially missed the nested loop.
        """
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0] = dp[1] = False
        for i in range(2, n):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = False
        return sum(dp)
