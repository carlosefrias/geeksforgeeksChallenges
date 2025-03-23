# https://www.geeksforgeeks.org/problems/total-decoding-messages1235/1
# A message containing letters A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# You are given a string digits. You have to determine the total number of ways that message can be decoded.

def count_ways(digits):
    if not digits or digits[0] == '0':
        return 0
    
    n = len(digits)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        one_digit = int(digits[i-1:i])
        two_digits = int(digits[i-2:i])
        
        if 1 <= one_digit <= 9:
            dp[i] += dp[i-1]
        
        if 10 <= two_digits <= 26:
            dp[i] += dp[i-2]

    return dp[-1]

print(count_ways("123")) # 3
print(count_ways("90")) # 0
print(count_ways("105")) # 1
print(count_ways("05")) # 0
print(count_ways("36671106")) # 1
print(count_ways("42100")) # 0
print(count_ways("12519")) # 6

# Examples:
# 
# Input: digits = "123"
# Output: 3
# Explanation: "123" can be decoded as "ABC"(1, 2, 3), "LC"(12, 3) and "AW"(1, 23).
# Input: digits = "90"
# Output: 0
# Explanation: "90" cannot be decoded, as it's an invalid string and we cannot decode '0'.
# Input: digits = "05"
# Output: 0
# Explanation: "05" cannot be mapped to "E" because of the leading zero ("5" is different from "05"), the string is not a valid encoding message.
# Constraints:
# 1 ≤ digits.size() ≤ 103