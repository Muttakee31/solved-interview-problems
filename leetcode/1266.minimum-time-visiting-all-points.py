class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/minimum-time-visiting-all-points/
        """
        dist = 0
        for p in range(1, len(points)):
            x = abs(points[p][0] - points[p-1][0])
            y = abs(points[p][1] - points[p-1][1])
            dist += max(x, y)
        
        return dist