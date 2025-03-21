# https://www.geeksforgeeks.org/problems/coin-change2448/1
# Given an integer array coins[ ] representing different denominations of currency and an integer sum, 
# find the number of ways you can make sum by using different combinations from coins[ ]. 
# Note: Assume that you have an infinite supply of each type of coin. Therefore, you can use any coin as many times as you want.
# Answers are guaranteed to fit into a 32-bit integer. 

def count(coins, sum):
    if sum == 0:
        return 0
    if sum < min(coins):
        return -1
    
    dp = [0] * (sum + 1)
    dp[0] = 0
    for i in range(1, sum + 1):
        for coin in coins:
            if i - coin == 0:
                dp[i] += 1
                print(dp)

    return dp[sum-1] if dp[sum-1] != float('inf') else -1

print(count([1, 2, 3], 4)) # 4
# print(count([2, 5, 3, 6], 10)) # 5  s

# Examples:

# Input: coins[] = [1, 2, 3], sum = 4
# Output: 4
# Explanation: Four Possible ways are: [1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3].
# Input: coins[] = [2, 5, 3, 6], sum = 10
# Output: 5
# Explanation: Five Possible ways are: [2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5] and [5, 5].
# Input: coins[] = [5, 10], sum = 3
# Output: 0
# Explanation: Since all coin denominations are greater than sum, no combination can make the target sum.