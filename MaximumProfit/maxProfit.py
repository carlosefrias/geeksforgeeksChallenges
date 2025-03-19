# https://www.geeksforgeeks.org/problems/maximum-profit4657/1

# In the stock market, a person buys a stock and sells it on some future date. 
# You are given an array prices[] representing stock prices on different days and a positive integer k, find out the maximum profit a person can make in at-most k transactions.
# A transaction consists of buying and subsequently selling a stock and new transaction can start only when the previous transaction has been completed.

def maxProfit(prices, k):
    if isSortedDescending(prices):
        return 0
    
    n = len(prices)
    if n <= 1:
        return 0
    
    # Create a 2D array to store the maximum profit
    dp = [[0 for _ in range(n)] for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i - 1][j] - prices[j])
    
    return dp[k][n - 1]
    

def isSortedDescending(prices):
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            return False
    return True

print(maxProfit([10, 22, 5, 80], 2)) # 87
print(maxProfit([20, 580, 420, 900], 3)) # 1040
print(maxProfit([100, 90, 80, 50, 25], 1)) # 0

# Examples :

# Input: prices[] = [10, 22, 5, 80], k = 2
# Output: 87
# Explaination:
# 1st transaction: Buy at 10 and sell at 22. 
# 2nd transaction : Buy at 5 and sell at 80.
# Total Profit will be 12 + 75 = 87.

# Input: prices[] = [20, 580, 420, 900], k = 3
# Output: 1040
# Explaination: 
# 1st transaction: Buy at 20 and sell at 580. 
# 2nd transaction : Buy at 420 and sell at 900.
# Total Profit will be 560 + 480 = 1040.

#Input: prices[] = [100, 90, 80, 50, 25],  k = 1
#Output: 0
#Explaination: Selling price is decreasing continuously
#leading to loss. So seller cannot have any profit.