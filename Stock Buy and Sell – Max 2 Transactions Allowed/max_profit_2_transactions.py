# https://www.geeksforgeeks.org/problems/buy-and-sell-a-share-at-most-twice/1

# In daily share trading, a trader buys shares and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, 
# find out the maximum profit that a share trader could have made.
# You are given an array prices[] representing stock prices throughout the day. 
# Note that the second transaction can only start after the first one is complete (buy->sell->buy->sell).

def isSortedDescending(prices):
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            return False
    return True


def maxProfit(prices):
    n = len(prices)
    if(n < 2):
        return 0
    if(isSortedDescending(prices)):
        return 0
    dp = [[0 for _ in range(n)] for _ in range(2)]

    for i in range(0, 2):
        maxDiff = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], prices[j] + maxDiff)
            maxDiff = max(maxDiff, dp[i-1][j] - prices[j])
    return dp[1][-1]


print(maxProfit([10, 22, 5, 75, 65, 80])) # 87
print(maxProfit([2, 30, 15, 10, 8, 25, 80])) # 100

# Input: prices[] = [10, 22, 5, 75, 65, 80]
# Output: 87
# Explanation: 
# Trader will buy at 10 and sells at 22. 
# Profit earned in 1st transaction = 22 - 10 = 12. 
# Then he buys at 5 and sell at 80. 
# Profit earned in 2nd transaction = 80 - 5 = 75. 
# Total profit earned = 12 + 75 = 87. 

# Input: prices[] = [2, 30, 15, 10, 8, 25, 80]
# Output: 100
# Explanation: 
# Trader will buy at 2 and sells at 30. 
# Profit earned in 1st transaction = 30 - 2 = 28. 
# Then he buys at 8 and sell at 80. 
# Profit earned in 2nd transaction = 80 - 8 = 72. 
# Total profit earned = 28 + 72 = 100.