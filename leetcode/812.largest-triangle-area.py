class Solution:
    def calculateArea(self, p1, p2, p3):
        return abs((p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[0]*p3[1] - p2[0]*p1[1] - p3[0]*p2[1])/2)
        
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        n = len(points)
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    maxArea = max(maxArea, self.calculateArea(points[i], points[j], points[k]))
            
        
        return maxArea