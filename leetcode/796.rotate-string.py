class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        t = s
        i = 0
        while(i < len(s)):
            t = s[i:] + s[:i]
            if t == goal:
                break
            i += 1
        
        return i < len(s)