class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ht = heights[:]
        ht.sort()
        x = 0
        for i in range(len(heights)):
            x += 1 if heights[i] != ht[i] else 0
        
        return x