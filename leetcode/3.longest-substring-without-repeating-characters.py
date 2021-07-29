class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        https://leetcode.com/problems/longest-substring-without-repeating-characters/
        took longer than it should.
        keep track of the last appearance of a character using dictionary.
        if the distance is bigger than previous, add 1 to current.
        otherwise use the distance as current value.
        could be done without using DP.
        """
        cd = dict()
        n = len(s)
        if n == 0:
            return 0
        dp = [0]*(n+1)
        for i in range(1, n+1):
            last_position = cd.get(s[i-1], None)
            cd[s[i-1]] = i
            if last_position and i - last_position - 1 <= dp[i-1]:
                dp[i] = i - last_position
            else:
                dp[i] = dp[i-1] + 1
        return max(dp)