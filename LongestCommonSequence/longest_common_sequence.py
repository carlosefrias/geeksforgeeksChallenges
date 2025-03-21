# https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1
# longest-common-subsequence

# Given two strings s1 and s2, return the length of their longest common subsequence (LCS). 
# If there is no common subsequence, return 0.
# A subsequence is a sequence that can be derived from the given string by deleting some or no elements without changing the order of the remaining elements. 
# For example, "ABE" is a subsequence of "ABCDE".

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)] 
    for i in range(1, n+1):
        for j in range(1, m+1):
            letter_s1 = s1[i-1]
            letter_s2 = s2[j-1]
            if letter_s1 == letter_s2:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

print(lcs("ABCDGH", "AEDFHR")) # 3
print(lcs("ABC", "AC")) # 2
print(lcs("XYZW", "XYWZ")) # 3
print(lcs("YESBJ", "FASEGBZUVC")) # 2
print(lcs("XUFNWMMYBJ", "XJXMMKN")) # 3

# Examples:
# Input: s1 = "ABCDGH", s2 = "AEDFHR"
# Output: 3
# Explanation: The longest common subsequence of "ABCDGH" and "AEDFHR" is "ADH", which has a length of 3.
# Input: s1 = "ABC", s2 = "AC"
# Output: 2
# Explanation: The longest common subsequence of "ABC" and "AC" is "AC", which has a length of 2.
# Input: s1 = "XYZW", s2 = "XYWZ"
# Output: 3
# Explanation: The longest common subsequences of "XYZW" and "XYWZ" are "XYZ" and "XYW", both of length 3.

