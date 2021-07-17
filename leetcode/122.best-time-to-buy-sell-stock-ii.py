class Solution(object):
    def maxProfit(self, prices):
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
        the answer to find the consecutive bottom and peaks and sum their differences.
        and the sum process gets easier using telescopic method.
        tried to solve using dp. for no reason :/
        """
        maxPro = 0        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxPro += prices[i]-prices[i-1]            
        return maxPro