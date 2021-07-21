class Solution:
    """
    https://leetcode.com/problems/maximum-ice-cream-bars/
    """
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i=0
        while(i<len(costs) and coins>0):
            if costs[i] > coins:
                break
            coins -= costs[i]
            i+=1
        return i