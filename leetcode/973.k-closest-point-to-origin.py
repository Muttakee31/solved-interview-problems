class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        https://leetcode.com/problems/k-closest-points-to-origin/
        sort and return first k elements
        """
        points.sort(key = lambda x : x[0]*x[0] + x[1]*x[1])
        return points[:k]