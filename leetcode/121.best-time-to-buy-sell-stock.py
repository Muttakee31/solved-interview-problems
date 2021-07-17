def maxProfit(prices):
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    tried to implement dp for practice
    """
    dp = [0 for i in range(len(prices))]
    
    min = prices[0]
    dp[0] = 0
    for i, p in enumerate(prices):
        if min > p:
            min = p
        dp[i] = max(p - min, dp[i-1])
    
    return dp[len(prices)-1]