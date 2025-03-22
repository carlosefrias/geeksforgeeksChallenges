# You are given an array arr[] which represents houses arranged in a circle, where each house has a certain value. 
# A thief aims to maximize the total stolen value without robbing two adjacent houses.
# Determine the maximum amount the thief can steal.

# Note: Since the houses are in a circle, the first and last houses are also considered adjacent.

# Examples:

# Input: arr[] = [2, 3, 2]
# Output: 3
# Explanation: arr[0] and arr[2] can't be robbed because they are adjacent houses. Thus, 3 is the maximum value thief can rob.
# Input: arr[] = [1, 2, 3, 1]
# Output: 4
# Explanation: Maximum stolen value: arr[0] + arr[2] = 1 + 3 = 4
# Input: arr[] = [2, 2, 3, 1, 2]
# Output: 5
# Explanation: Maximum stolen value: arr[0] + arr[2] = 2 + 3 = 5 or arr[2] + arr[4] = 3 + 2 = 5

def find_max_sum(arr):
    def simple_rob(nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

    n = len(arr)
    if n == 1:
        return arr[0]
    return max(simple_rob(arr[:-1]), simple_rob(arr[1:]))

print(find_max_sum([3, 7, 6, 5, 8, 2, 7, 5, 2, 3, 5])) # 29
print(find_max_sum([4, 9, 1, 2, 6, 2, 7, 2, 2, 6])) # 28
print(find_max_sum([2, 3, 2])) # 3
print(find_max_sum([1, 2, 3, 1])) # 4
print(find_max_sum([2, 2, 3, 1, 2])) # 5