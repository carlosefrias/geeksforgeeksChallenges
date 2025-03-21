# https://www.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1
#There are n stairs, a person standing at the bottom wants to reach the top. 
# The person can climb either 1 stair or 2 stairs at a time. Your task is to count the number of ways, the person can reach the top (order does matter).

def countWays(n):
    dp = [0]*n
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    dp[0]=1
    dp[1]=2
    for i in range(2,n):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[-1]


print(countWays(4)) #5
print(countWays(1)) #1
print(countWays(2)) #2
print(countWays(3)) #3

# Examples:

# Input: n = 1
# Output: 1
# Explanation: There is only one way to climb 1 stair. 
# Input: n = 2
# Output: 2
# Explanation: There are 2 ways to reach 2th stair: {1, 1} and {2}.  
# Input: n = 4
# Output: 5
# Explanation: There are five ways to reach 4th stair: {1, 1, 1, 1}, {1, 1, 2}, {2, 1, 1}, {1, 2, 1} and {2, 2}.