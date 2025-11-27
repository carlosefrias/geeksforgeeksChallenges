# Max Sum Increasing Subsequence
# Difficulty: MediumAccuracy: 40.02%Submissions: 220K+Points: 4Average Time: 25m
# Given an array of positive integers arr[], find the maximum sum of a subsequence such that the elements of the subsequence form a strictly increasing sequence.
# In other words, among all strictly increasing subsequences of the array, return the one with the largest possible sum.

# Examples:

# Input: arr[] = [1, 101, 2, 3, 100]
# Output: 106
# Explanation: The maximum sum of an increasing sequence is obtained from [1, 2, 3, 100].
# Input: arr[] = [4, 1, 2, 3]
# Output: 6
# Explanation: The maximum sum of an increasing sequence is obtained from [1, 2, 3].
# Input: arr[] = [4, 1, 2, 4]
# Output: 7
# Explanation: The maximum sum of an increasing sequence is obtained from [1, 2, 4].
# Constraints:
# 1 ≤ arr.size() ≤ 103
# 1 ≤ arr[i] ≤ 105

# Expected Complexities
# Time Complexity: O(n log n)
# Auxiliary Space: O(n)
class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        dp = [0]*n
        for i in range(n):
            dp[i] = arr[i]
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + arr[i])
        return max(dp)

sol = Solution()

print(sol.maxSumIS([1, 101, 2, 3, 100]))
print(sol.maxSumIS([4, 1, 2, 3]))
print(sol.maxSumIS([4, 1, 2, 4]))