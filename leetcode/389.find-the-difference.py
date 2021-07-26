class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = list(map(ord, s))
        y = list(map(ord, t))
        return chr(sum(y)-sum(x))