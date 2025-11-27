# Longest Common Increasing Subsequence
# Difficulty: MediumAccuracy: 40.62%Submissions: 21K+Points: 4
# Given two arrays, a[] and b[], find the length of the longest common increasing subsequence(LCIS).

# Note:  LCIS refers to a subsequence that is present in both arrays and strictly increases.

# Examples:

# Input: a[] = [3, 4, 9, 1], b[] = [5, 3, 8, 9, 10, 2, 1]
# Output: 2
# Explanation: The longest increasing subsequence that is common is [3, 9] and its length is 2.
# Input: a[] = [1, 1, 4, 3], b[] = [1, 1, 3, 4]
# Output: 2
# Explanation: There are two common subsequences [1, 4] and [1, 3] both of length 2.
# Constraints:
# 1 ≤ a.size(), b.size() ≤ 103
# 1 ≤ a[i], b[i] ≤ 104

# Expected Complexities
# Time Complexity: O(n * m)
# Auxiliary Space: O(n)
class Solution:
    def LCIS(self, a, b):
        n, m = len(a), len(b)
        dp = [0] * m

        for i in range(n):
            current = 0
            for j in range(m):
                if a[i] == b[j]:
                    dp[j] = max(dp[j], current + 1)
                    print(dp)
                elif a[i] > b[j]:
                    current = max(current, dp[j])
        return max(dp) if dp else 0

sol = Solution()
a = [3, 4, 9, 1]
b = [5, 3, 8, 9, 10, 2, 1]

print(sol.LCIS(a, b))

a, b = [1, 1, 4, 3], [1, 1, 3, 4]
print(sol.LCIS(a, b))
