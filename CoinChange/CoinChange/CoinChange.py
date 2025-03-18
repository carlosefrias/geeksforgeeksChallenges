def min_coins(coins, target):
    if target == 0:
        return 0
    if target < min(coins):
        return -1
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1

if __name__ == "__main__":
    print(min_coins([30, 20, 5], 25))
    print(min_coins([25, 10, 5], 30))
    print(min_coins([9, 6, 5, 1], 19))
    print(min_coins([5, 1], 0))
    print(min_coins([4, 6, 2], 5))
    print(min_coins([25, 20, 10, 10, 2, 1], 40))
    print(min_coins([18, 15, 16, 20], 27))

# Coins = [25, 20, 10, 10, 2, 2, 1]
# Target 40
# You are given an array coins[], where each element represents a coin of a different denomination, and a target value sum.
# You have an unlimited supply of each coin type {coins1, coins2, ..., coinsm}.
#
# Your task is to determine the minimum number of coins needed to obtain the target sum.
# If it is not possible to form the sum using the given coins, return -1.
#
# 				Examples:
#
# Input: coins[] = [25, 10, 5], sum = 30
# Output: 2
# Explanation: Minimum 2 coins needed, 25 and 5  
# Input: coins[] = [9, 6, 5, 1], sum = 19
# Output: 3
# Explanation: 19 = 9 + 9 + 1
# Input: coins[] = [5, 1], sum = 0
# Output: 0
# Explanation: For 0 sum, we do not need a coin
# Input: coins[] = [4, 6, 2], sum = 5
# Output: -1
# Explanation: Not possible to make the given sum.
#  
# 				Constraints:
# 1 ≤ sum * coins.size() ≤ 106
# 0 <= sum <= 104
# 1 <= coins[i] <= 104
# 1 <= coins.size() <= 103
