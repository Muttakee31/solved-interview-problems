from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        https://leetcode.com/problems/robot-return-to-origin/
        """
        co = Counter(moves)
        return co['U'] == co['D'] and co['R'] == co['L']