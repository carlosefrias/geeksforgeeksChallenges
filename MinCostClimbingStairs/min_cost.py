# https://www.geeksforgeeks.org/problems/min-cost-climbing-stairs/1
# Given an array of integers cost[] where cost[i] is the cost of the ith step on a staircase. Once the cost is paid, you can either climb one or two steps. Return the minimum cost to reach the top of the floor.
# Assume 0-based Indexing. You can either start from the step with index 0, or the step with index 1.

def minCostClimbingStairs(cost):
        #Write your code here
        n = len(cost)
        if n==0:
            return 0
        if n==1:
            return cost[0]
        if n==2:
            return min(cost[0], cost[1])
        dp = [0 for _ in range(n)]
        for i in range(0, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])


print(minCostClimbingStairs([10, 15, 20])) # 15
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) # 6

# Input: cost[] = [10, 15, 20]
# Output: 15
# Explanation: Cheapest option is to start at cost[1], pay that cost, and go to the top.

# Input: cost[] = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest option is to start on cost[0], and only step on 1s, skipping cost[3].